#!/usr/bin/env python

#roslaunch turtlebot_stage turtlebot_in_stage.launch map_file:="/home/ros/catkin_ws/src/exercise3/scripts/maze3.yaml" world_file:="/home/ros/catkin_ws/src/exercise3/scripts/maze3.world" initial_pose_x:=5.0 initial_pose_y:=5.0 initial_pose_a:=0.0

import rospy
#for applying markers
import roslib; roslib.load_manifest('visualization_marker_tutorials')
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
from std_msgs.msg import ColorRGBA


### PYTHON IMPORTS ####
import numpy as np
from bisect import bisect_left
import pdb
import matplotlib.pyplot as plt

### Sensor Messages ####
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

messages_skip = 0
messages_to_skip = 10
marker_list = list()

line_counter = 0

def hough_circle(angles, ds):

	plot_on = False

	angle_min = 0
	angle_max = np.pi * 2
	angle_step = 0.1 #grid size
	angle_range = np.arange(angle_min, angle_max, angle_step, float)
	angle_indx = np.arange(len(angle_range))

	r_min = 0
	r_max = 4 #may need to increase this if objects in the world are large
	r_step = 0.3
	r_range = np.arange(r_min, r_max, r_step, float)
	r_indx = np.arange(len(r_range))

	c_a_min = 0
	c_a_max = 5
	c_a_step = 1
	c_a_range = np.arange(c_a_min, c_a_max, c_a_step, float)
	c_a_indx = np.arange(len(c_a_range))

	c_b_min = 0
	c_b_max = 5
	c_b_step = 1
	c_b_range = np.arange(c_b_min, c_b_max, c_b_step, float)
	c_b_indx = np.arange(len(c_b_range))

	#the array that will be used to count
	accumulator = np.zeros([len(c_a_range), len(c_b_range), len(r_range)])

	for a,d in zip(angles,ds):
		#convert points from cloud into x,y points
		if int(d) != 5: #filtering out max values
			x = d*np.cos(a)
			y = d*np.sin(a)
			theta_count = 0
			#find curve in theta-rho space
			for r in r_indx:
				for a in c_a_indx:
					for b in c_b_indx:
						left_side = (x-c_a_range[a])**2 + (y-c_b_range[b])**2
						right_side = r_range[r]**2
						if abs(left_side - right_side)  < 1: #some tolerance because method is not exact
							accumulator[a, b, r] += 1
		
	#find most likely line
	brightest = np.amax(accumulator)
	#normalize plot so that largest value is maximum brightness
	brightest_indx = np.argmax(accumulator) #getting features of largets values by location in matrix
	circle = np.unravel_index(brightest_indx, accumulator.shape)
	#return circle center and radius relative to robot scan frame
	c_a = c_a_range[circle[0]]
	c_b = c_b_range[circle[1]]
	r   = r_range[circle[2]]
	print [c_a, c_b, r]
	if plot_on == True:
		plt.figure()
		xs, ys = np.meshgrid(angle_range, r_range, indexing = 'ij')
		zs = norm_accumulator
		plt.pcolor(xs, ys, zs[:-1, :-1], cmap = 'gray')
		plt.plot(angle_range[line[0]], r_range[line[1]], 'ro')
		plt.show()

	if [c_a, c_b] in marker_list: #need to add some tolerance because points won't be consistent
		print('Already seen marker')
	else:
		marker_list.append([c_a, c_b]) #add marker to list
		pub_str = str(c_a) + ',' + str(c_b) #center point
		object_pub.publish(pub_str)

	return [c_a, c_b, r] #this is where the marker go RELATIVE TO ROBOT FRAME!!


def callback_scan(data):
	#because hough transform is so slow, only process every N message
	global messages_skip

	#holders
	r_vals = np.array(list())
	points = np.array(list())

	#getting range of angles
	angle_min = data.angle_min
	angle_max = data.angle_max
	angle_increment = data.angle_increment
	t_vals = np.arange(angle_min, angle_max + angle_increment, angle_increment) #include one more value so arrays are same length

	# get distance values from scan data
	r_vals     = np.array(data.ranges, float)


	# print('Callback Activated!' + str(Hough_lock))
	if messages_skip < messages_to_skip:
		messages_skip += 1
	elif messages_skip == messages_to_skip:
		messages_skip = 0
		circle       = hough_circle(t_vals, r_vals)


if __name__ == '__main__':
	
	rospy.init_node('hough_transform')

	#A subscriber for the scan data
	rospy.Subscriber('scan', LaserScan, callback_scan)
	# marker_pub = rospy.Publisher('/visualization_marker', Marker, queue_size = 10)
	object_pub = rospy.Publisher('/object_location', String, queue_size = 10)


	run_flag = True
	while run_flag:
		try: 
			rate = rospy.Rate(10)
			while not rospy.is_shutdown():
				rate.sleep()

		except KeyboardInterrupt:
			print("Ctrl-C caught.  Quitting!")
			rospy.signal_shutdown('Done!')
			run_flag = False

	
	rospy.signal_shutdown('Done!')

