/*
Emily Longman
4/24/17

Based largely off:
https://tnichols.org/2015/10/19/Hooking-the-Linux-System-Call-Table/
https://tc.gtisc.gatech.edu/bss/2014/r/kernel-exploits.pdf
*/

#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/unistd.h>
#include <linux/fs.h>
#include <linux/slab.h>
#include <asm/paravirt.h>
#include <asm/uaccess.h> 
#include "hooks.h"
#define PROC_V    "/proc/version"
#define BOOT_PATH "/boot/System.map-"
#define MAX_VERSION_LEN   256

unsigned long *syscall_table = NULL;
//unsigned long *syscall_table = (unsigned long *)0xffffffff81801400;
asmlinkage int (*original_write)(unsigned int, const char __user *, size_t);
static int find_sys_call_table (char *kern_ver) {
    char system_map_entry[MAX_VERSION_LEN];
    int i = 0;

    char *filename; // Holds the /boot/System.map-<version> file name as we build it
    size_t filename_length = strlen(kern_ver) + strlen(BOOT_PATH) + 1; // Length of the System.map filename, terminating NULL included
    struct file *f = NULL; // This will point to our /boot/System.map-<version> file
 
    mm_segment_t oldfs;
    oldfs = get_fs();
    set_fs (KERNEL_DS);
    printk(KERN_EMERG "Kernel version: %s\n", kern_ver);
     
    filename = kmalloc(filename_length, GFP_KERNEL);
    if (filename == NULL) {
        printk(KERN_EMERG "kmalloc failed on System.map-<version> filename allocation");
        return -1;
    }
     
    memset(filename, 0, filename_length);
     
    //Construct /boot/System.map-<version> file name
    strncpy(filename, BOOT_PATH, strlen(BOOT_PATH));
    strncat(filename, kern_ver, strlen(kern_ver));
     

    f = filp_open(filename, O_RDONLY, 0);
    if (IS_ERR(f) || (f == NULL)) {
        printk(KERN_EMERG "Error opening System.map-<version> file: %s\n", filename);
        return -1;
    } 
    memset(system_map_entry, 0, MAX_VERSION_LEN);

    // Read through memory 
    while (vfs_read(f, system_map_entry + i, 1, &f->f_pos) == 1) {

        if ( system_map_entry[i] == '\n' || i == MAX_VERSION_LEN ) {
            // Reset the "column"/"character" counter for the row
            i = 0;
             
            if (strstr(system_map_entry, "sys_call_table") != NULL) {
                char *sys_string;
                char *system_map_entry_ptr = system_map_entry;
                 
                sys_string = kmalloc(MAX_VERSION_LEN, GFP_KERNEL);  
                if (sys_string == NULL) { 
                    filp_close(f, 0);
                    set_fs(oldfs);
                    kfree(filename);
     
                    return -1;
                }
 
                memset(sys_string, 0, MAX_VERSION_LEN);
                strncpy(sys_string, strsep(&system_map_entry_ptr, " "), MAX_VERSION_LEN);
             
                //syscall_table = (unsigned long long *) kstrtoll(sys_string, NULL, 16);
                //syscall_table = kmalloc(sizeof(unsigned long *), GFP_KERNEL);
                //syscall_table = kmalloc(sizeof(syscall_table), GFP_KERNEL);
                kstrtoul(sys_string, 16, &syscall_table);
                printk(KERN_EMERG "syscall_table retrieved\n");
                 
                kfree(sys_string);
                 
                break;
            }
             
            memset(system_map_entry, 0, MAX_VERSION_LEN);
            continue;
        }
         
        i++;
    }
 
    filp_close(f, 0);
    set_fs(oldfs);
     
    kfree(filename);
 
    return 0;
}

char *acquire_kernel_version (char *buf) {
    struct file *proc_version;
    char *kernel_version;
  
    // Store userspace perspective
    mm_segment_t oldfs;

    // Read file into kernel space
    oldfs = get_fs();
    set_fs (KERNEL_DS);
  
    proc_version = filp_open(PROC_V, O_RDONLY, 0);
    if (IS_ERR(proc_version) || (proc_version == NULL)) {
        return NULL;
    }

    memset(buf, 0, MAX_VERSION_LEN);
  
    vfs_read(proc_version, buf, MAX_VERSION_LEN, &(proc_version->f_pos));
  
    kernel_version = strsep(&buf, " ");
    kernel_version = strsep(&buf, " ");
    kernel_version = strsep(&buf, " ");
  
    filp_close(proc_version, 0);
    
    // Switch back to userspace
    set_fs(oldfs);
  
    return kernel_version;
}

asmlinkage int new_write (unsigned int x, const char __user *y, size_t size) {
    printk(KERN_EMERG "[+] write() hooked.");
  
    return original_write(x, y, size);
}

static int __init onload(void) {
    char *kernel_version = kmalloc(MAX_VERSION_LEN, GFP_KERNEL);
    printk(KERN_WARNING "Made it in\n");
    // printk(KERN_EMERG "Version: %s\n", acquire_kernel_version(kernel_version));
  
    find_sys_call_table(acquire_kernel_version(kernel_version));
  
    printk(KERN_EMERG "Syscall table address: %p\n", syscall_table);
    printk(KERN_EMERG "sizeof(unsigned long *): %zx\n", sizeof(unsigned long*));
    printk(KERN_EMERG "sizeof(sys_call_table) : %zx\n", sizeof(syscall_table));
  
    if (syscall_table != NULL) {
        write_cr0 (read_cr0 () & (~ 0x10000));
        original_write = (void *)syscall_table[__NR_write];
        syscall_table[__NR_write] = &new_write;
        write_cr0 (read_cr0 () | 0x10000);
        printk(KERN_EMERG "[+] onload: sys_call_table hooked\n");
    } else {
        printk(KERN_EMERG "[-] onload: syscall_table is NULL\n");
    }
  
    kfree(kernel_version);
  
    return 0;
}

static void __exit onunload(void) {
    if (syscall_table != NULL) {
        write_cr0 (read_cr0 () & (~ 0x10000));
        syscall_table[__NR_write] = original_write;
        write_cr0 (read_cr0 () | 0x10000);
        printk(KERN_EMERG "[+] onunload: sys_call_table unhooked\n");
    } else {
        printk(KERN_EMERG "[-] onunload: syscall_table is NULL\n");
    }
    printk(KERN_INFO "Exiting\n");
}

module_init(onload);
module_exit(onunload);