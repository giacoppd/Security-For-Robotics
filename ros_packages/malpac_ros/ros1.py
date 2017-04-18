#!/usr/bin/python
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
##             ROS Package 1 - Broken Authentication
##                         ros1.py
###################################################################################
import os
import rospy

#ROS Environment Variables -- Will need to change these accordingly
ROS_CORE_PORT = "1337"
VICTIM_ROS_HOSTNAME = "http://192.168.0.10"
VICTIM_ROS_MASTER_URI = VICTIM_ROS_HOSTNAME + ":" + ROS_CORE_PORT

ATTACKER_ROS_MASTER_URI = VICTIM_ROS_MASTER_URI
ATTACKER_ROS_HOSTNAME = "http://192.168.0.11"

#IS THIS SCRIPT RUNNING ON THE ATTACKER OR VICTIM MACHINE?
#When set to VICTIM, the PoC will establish the victim side of the equation
#When set to ATTACKER, the PoC will setup the attacker side of the equation
#Use sys args instead?
WHOAMI = "VICTIM"

#Should we be loud and proud?
VERBOSE = True

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

if __name__ == '__main__':
    main()
