#!/usr/bin/env python
# license removed for brevity
import rospy
import time
from std_msgs.msg import String

#def talker():
#	pub = rospy.Publisher('chatter', String, queue_size=10)
#	rospy.init_node('talker', anonymous=True)
#	rate = rospy.Rate(10) # 10hz
#	while not rospy.is_shutdown():
#		hello_str = "hello world %s" % rospy.get_time()
#		rospy.loginfo(hello_str)
#		pub.publish(hello_str)
#		rate.sleep()

def fib(n):
	rospy.init_node('fib', anonymous=True)
	if n == 1:
		return 1
	else:
		return fib(n-2) + fib(n-1)

if __name__ == '__main__':
	try:
		rospy.loginfo("Fib is going to print at some point.")
		rospy.loginfo(fib(1000000))
	except rospy.ROSInterruptException:
		pass
