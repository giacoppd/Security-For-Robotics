#!/usr/bin/env python2
import rospkg
import rospy
import time
from std_msgs.msg import Int32

def notmain():
	cur_int = Int32(0)
	rospy.init_node('adder', anonymous=True)
	pub = rospy.Publisher('addout', Int32, queue_size=10)
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		cur_int.data = cur_int.data+1
		rospy.loginfo(cur_int)
		pub.publish(cur_int)
		time.sleep(5)
		rate.sleep()

if __name__ == '__main__':
	notmain()
