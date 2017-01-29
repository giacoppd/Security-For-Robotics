#!/usr/bin/env python
# Every python controller needs these lines
import rospy

# The velocity command message
from geometry_msgs.msg import Twist
# The sensor data messages
from sensor_msgs.msg import LaserScan

minDist = 10000
command = None

def obstacleCallback(val):
	#Will get the closest distance
	closeDist = min(val.ranges)
	global minDist
	minDist = closeDist
	#print minDist
	
def keyboardCallback(val):
	#print 'keyboardCallback reached!!!'
	#rospy.logdebug('keyboardCallback reached!!!')
	rospy.logdebug(val)
	global command
	command = val

def driver(command):
	#print command
	if minDist <= 0.52 and (command.linear.x > 0 or command.angular.x > 0):
		print 'Not allowed to move forward because of wall'
		rospy.logdebug('Not allowed to move forward because of there is a wall\n')
		command.linear.x = 0.0
		command.linear.y = 0.0
		command.linear.z = 0.0
		command.angular.x = 0.0
		command.angular.y = 0.0
		command.angular.z = 0.0
		rospy.logdebug(command)
	elif minDist <= 0.52 and (command.linear.x < 0 or command.angular.x < 0):
		print 'Allowed because going backwards'
		rospy.logdebug('Allowed because going backwards\n')
		command.linear.x = -0.1
		command.linear.y = 0.0
		command.linear.z = 0.0
		command.angular.x = 0.0
		command.angular.y = 0.0
		command.angular.z = 0.0
		rospy.logdebug(command)

	# print command
	return command		


if __name__ == '__main__':
	rospy.init_node('move')

	# A publisher for the move data
	pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist)
	rospy.Subscriber("scan", LaserScan, obstacleCallback)
	rospy.Subscriber("tele", Twist, keyboardCallback)

	# Drive forward at a given speed.  The robot points up the x-axis.
	global command
	command = Twist()

	command.linear.x = 0.0
	command.linear.y = 0.0
	command.linear.z = 0.0
	command.angular.x = 0.0
	command.angular.y = 0.0
	command.angular.z = 0.0

	# Loop at 10Hz, publishing movement commands until we shut down.
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		global command
		comm = driver(command)
		pub.publish(comm)
		rate.sleep()

