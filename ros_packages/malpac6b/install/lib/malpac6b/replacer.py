#!/usr/bin/env python2
#this isn't important enough to license
#Starts a "good" node in a different package, lets it run for 10 seconds, then kills it and runs a node with the same name from a different package
#assumes your on ROS indigo
import os
import rospy
import time

def swapper():
    os.system("source /opt/ros/indigo/setup.bash")
    os.system("export PYTHONPATH=/opt/ros/indigo/lib/python2.7/site-packages:$PYTHONPATH")
    os.system('export PKG_CONFIG_PATH="/opt/ros/indigo/lib/pkgconfig:$PKG_CONFIG_PATH"')
    os.system('export ROS_HOSTNAME=localhost')
    os.system("export ROS_MASTER_URI=http://localhost:11311")
    os.system("source ../malpac6/install/setup.bash")
    os.system("cd ../")
    os.system('catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python2 -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so')
    os.system("rosrun malpac6 dummy.py &")
    time.sleep(10)
    os.system("kill $(ps aux | grep dummy.py | grep -v grep | awk '{print $2}')")
    os.system("rosrun malpac6b dummy.py")

if __name__ == '__main__':
    swapper()
