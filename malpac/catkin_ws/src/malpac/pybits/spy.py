#!/usr/bin/env python2
import rospkg
import rospy
from std_msgs.msg import Int32

def printer(data):
	rospy.loginfo("saw %s", data.data)
	print('I see' + str(data.data))
	rospy.spin() #why doesn't it keep running

def notmain():
	rospy.init_node('spy', anonymous=True)
	rospy.Subscriber('addout', Int32, printer)

if __name__ == '__main__':
	notmain()
