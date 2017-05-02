## OS Level Exploits

#### mem_hooks.c

So technically speaking this is actually a Linux kernel exploit, and doesn't use ROS itself, but ROS commonly sits atop Ubuntu or Ubuntu-based linux systems. This package does a simple memory hook into the syscall table, which allows the script to make changes to whichever syscalls it wants once it finds the syscall table memory address. This is done by changing the pointer to the function of an existing syscall and replacing it with a pointer to a malicious function.

This is the kind of script that would likely be secondary to one of the network attacks. One of those might be used to get into the system, and could then install LKMs like this one. Since it operates at the kernel level in Linux, ROS would have no way of ever knowing something was amiss, which renders this a very insidious threat.

#### stack_smash.c

This script provides a basic proof of concept for stack smashing! This is a form of buffer overflow attack which has been used reliably for a very long time to gain unauthorized access to a system. This specific script is a small scale buffer so better demonstrate the idea. To use a simple approach like this, one needs access to the environment variables of the system so it's not perfect. There's still room for improvement to make this script more generalizable.
