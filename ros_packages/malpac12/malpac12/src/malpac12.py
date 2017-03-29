#!/usr/bin/env python2
#this isn't important enough to license
#should remove ros on most debian/ubuntu systems.
#like in theory, our drone
import os
import rospy

def delros():
	os.system('apt-get remove "^ros.*" --force-yes')

if __name__ == '__main__':
    delros()
