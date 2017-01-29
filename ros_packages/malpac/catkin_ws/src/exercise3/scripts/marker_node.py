#!/usr/bin/env python

import rospy

### Sensor Messages ####
from std_msgs.msg import String
from visualization_msgs.msg import Marker


### PYTHON IMPORTS ####
import pdb
import numpy as np


def callback_scan(data):
	print('Displaying Markers')
	points_str = data.data
	# pdb.set_trace()
	points = points_str.split(',')
	points = np.array(points, float)
	sphere_marker = Marker()
	sphere_marker.type = Marker.SPHERE
	sphere_marker.id = np.random.randint(100000)
	sphere_marker.action = Marker.ADD
	sphere_marker.header.frame_id = 'base_link'
	sphere_marker.ns = 'hw2'
	sphere_marker.lifetime = rospy.Duration(30)

	sphere_marker.pose.position.x = points[0]
	sphere_marker.pose.position.y = points[1]
	sphere_marker.pose.position.z = 0
	# sphere_marker.pose.orientation.x = 0
	# sphere_marker.pose.orientation.y = 0
	# sphere_marker.pose.orientation.z = 0
	# sphere_marker.pose.orientation.w = 0

	print sphere_marker.pose.position

	sphere_marker.scale.x = 0.5
	sphere_marker.scale.y = 0.5
	sphere_marker.scale.z = 0.5
	sphere_marker.color.a = 1
	sphere_marker.color.r = 255
	sphere_marker.color.b = 0
	sphere_marker.color.g = 255

	marker_pub.publish(sphere_marker)


if __name__ == '__main__':
	
	rospy.init_node('hough_marker')

	#A subscriber for the scan data
	rospy.Subscriber('object_location', String, callback_scan)
	#Publishig for markers
	marker_pub = rospy.Publisher('/circle_markers', Marker, queue_size = 10)


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