#!/usr/bin/env python2
#this isn't important enough to license
#prints a message to stdout every 5 seconds
import os
import rospy
import time

def fafabout():
    while(True):
        os.system("echo I am not important but I could be")
        time.sleep(5)

if __name__ == '__main__':
    fafabout()
