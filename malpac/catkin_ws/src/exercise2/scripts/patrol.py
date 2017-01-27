#!/usr/bin/env python
# Every python controller needs these lines
import rospy
import actionlib
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import ast
import time
import random

start = 0
change = 0
waypoints = []
base = [(1.0, 3.0, 0.0), (0.0, 0.0, 0.0, 1.0)]
#[(2.1, 2.2, 0.0), (0.0, 0.0, 0.0, 1.0)]

def randomizeWays(ways):
	print "I'll randomize my ways"
	random.shuffle(ways)
	print ways
	return ways

def obstacleCallback(val):
	#Will get the closest distance
	closeDist = min(val.ranges)
	if change == 2:
		print 'Closest thing is ' + str(closeDist) + ' m away.'
		global change
		change  = 0

def goal_pose(pose):  # <2>
	goal_pose = MoveBaseGoal()
	goal_pose.target_pose.header.frame_id = 'map'
	goal_pose.target_pose.pose.position.x = pose[0][0]
	goal_pose.target_pose.pose.position.y = pose[0][1]
	goal_pose.target_pose.pose.position.z = pose[0][2]
	goal_pose.target_pose.pose.orientation.x = pose[1][0]
	goal_pose.target_pose.pose.orientation.y = pose[1][1]
	goal_pose.target_pose.pose.orientation.z = pose[1][2]
	goal_pose.target_pose.pose.orientation.w = pose[1][3]

	return goal_pose

def interesting(count, pose):
	if count == 0:
		print "Officer Roomba ready for patrolling duty!" 
	elif count == 1:
		left = len(waypoints) - waypoints.index(pose) - 1
		print 'I have ' + str(left) + ' waypoints left to go.'
	elif count == 2:
		print "I'm skeptical of what is near. I'm going to start checking who or what is close by."
		global change
		change = 2
		rospy.Subscriber("scan", LaserScan, obstacleCallback)
	elif count == 3:
		global start
		print "I spent " + str(time.time()-start) + " secs running around."
		print 'I need a break...'
		print "I'm going to hang around here for a little bit."

		time.sleep(10)

def need2send(msg):
	if msg.data == 'r':
		print 'Going to randomize waypoints'
		global waypoints
		randomizeWays(waypoints)
	elif msg.data == 'h':
		print 'I need to return to base'
		client = actionlib.SimpleActionClient('move_base', MoveBaseAction)  # <3>
		client.wait_for_server()
		client.send_goal(goal_pose(base))
		client.send_goal(goal_pose(base))
		client.send_goal(goal_pose(base))
		client.wait_for_result()

def dothis():

	client = actionlib.SimpleActionClient('move_base', MoveBaseAction)  # <3>
	client.wait_for_server()

	rospy.Subscriber('keys', String, need2send) #, sendmsg)

	global start
	start = time.time()

	while True:
		global waypoints
		for i, pose in enumerate(waypoints):   # <4>
			rospy.Subscriber('keys', String, need2send) #, sendmsg)
			print 'Going to ' + str(pose)
			goal = goal_pose(pose)
			client.send_goal(goal)
			client.wait_for_result()
			interesting(i, pose)

if __name__ == '__main__':
	rospy.init_node('patrol')

	with open("/home/ros/catkin_ws/src/exercise2/src/waypoints.txt", "r") as ways:
		for line in ways:
			global waypoints
			waypoints.append(ast.literal_eval(line))

	dothis()