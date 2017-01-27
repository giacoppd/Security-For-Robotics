#!/usr/bin/env python
# Written by Patrick Clary <claryp@oregonstate.edu>
# Part of programming assignment 3 for ROB 514

import rospy
from geometry_msgs.msg import PointStamped
from actionlib_msgs.msg import GoalStatusArray

coords = [[ 0.0,  0.0],
          [10.0,  0.0],
          [10.0, 10.0],
          [ 0.0, 10.0],
          [ 0.0,  0.0],
          [ 5.0,  5.0]]

status = 0

def callback(data):
    global status
    if data.status_list:
        status = data.status_list[-1].status

if __name__ == '__main__':
    rospy.init_node('set_border')
    pub = rospy.Publisher('/clicked_point', PointStamped, queue_size=10)
    sub = rospy.Subscriber('/explore_server/status', GoalStatusArray, callback)
    rate = rospy.Rate(2)
    rospy.sleep(1)

    while not rospy.is_shutdown():
        if status != 1:
            for c in coords:
                p = PointStamped()
                p.header.frame_id = 'map'
                p.point.x = c[0]
                p.point.y = c[1]
                pub.publish(p)
                rate.sleep()
        rospy.sleep(1)
