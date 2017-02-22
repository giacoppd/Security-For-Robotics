#!/usr/bin/env python2
#this isn't important enough to license
#prints a message to stdout every 5 seconds
import os
import rospy
import time

def switcher():
        os.system("roslaunch dummy malpac6.launch")
        os.system("kill $(ps aux | grep dummy.py | grep -v grep | awk '{print $2}')")
        os.system("roslaunch replacer malpac6.launch")

if __name__ == '__main__':
    switcher()
