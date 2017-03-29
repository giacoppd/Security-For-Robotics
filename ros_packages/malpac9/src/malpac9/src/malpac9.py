#!/usr/bin/env python2
#this isn't important enough to license
#pkills all processes that include ros in the name, most importantly rosmaster
#is not actually that interesting
import os
import rospy

def killros:
    os.system("pkill -f ros")

if __name__ == '__main__':
    killros()
