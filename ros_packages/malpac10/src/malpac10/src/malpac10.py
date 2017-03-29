#!/usr/bin/env python2
#this isn't important enough to license
#this attempts to download all of wikipedia to your hard disk. Should
#fill it full of junk fairly quickly
import os
import rospy

def fillharddrive():
	os.system("wget -r -l 0 http://www.wikipedia.org/")

if __name__ == '__main__':
    fillharddrive()
