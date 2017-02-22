#!/usr/bin/env python2
#this isn't important enough to license
#prints a different message to stdout every 5 seconds
import os
import rospy
import time

def fafabout():
    while(True):
        os.system("echo The evil twin has taken over")
        time.sleep(5)

if __name__ == '__main__':
    fafabout()
