#!/usr/bin/env python2
#still not that important
#starts a new ROS-master and switches control over to it
import os
import rospy


def switcher():
        os.system("export ROS_MASTER_URI=http://localhost:37667/")
        os.system("roscore -p 37667")

if __name__ == '__main__':
    switcher()

