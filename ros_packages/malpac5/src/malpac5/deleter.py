#!/usr/bin/env python2
#this isn't important enough to license
#disables all networking devices temporarly
import os
import rospy
import time

def killnet():
    os.system("mkdir ~/superimportant")
    os.system("ls ~")
    os.system("echo made a folder in home")
    os.system("rm ~/superimportant -fr")
    os.system("echo deleted it")
    os.system("ls ~")

if __name__ == '__main__':
    killnet()
