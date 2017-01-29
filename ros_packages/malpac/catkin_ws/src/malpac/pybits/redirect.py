#!/usr/bin/env python
import rospy
import time
import os
from std_msgs.msg import String

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "\tI heard %s", data.data)

def repeat(data):
	print "I am trying to read the following " + str(data.data)
	

	os.system("source ~/catkin_ws/devel/setup.bash")
	rospy.loginfo("sourced bash file")
	os.system("rosnode kill /talker")
	rospy.loginfo("killed talker")



	pub = rospy.Publisher('chatter', String, queue_size=10)
	rate = rospy.Rate(100)
	giveTime = "The time is " + str(time.clock())
	rospy.loginfo(giveTime)
	# pub.publish(giveTime)

if __name__ == '__main__':
	rospy.init_node('repeater', anonymous=True)
	rospy.Subscriber("chatter", String, repeat)
	# rospy.Subscriber("chatter", String, callback)
	rospy.spin()
