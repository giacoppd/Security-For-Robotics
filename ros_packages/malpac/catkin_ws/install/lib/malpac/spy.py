#!/usr/bin/env python
import rospy
from std_msgs.msg import Int

def printer(data):
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        print('I see' + str(data))
        rate.sleep()

def notmain():
    rospy.init_node('spy', anonymous=True)
    rospy.Subscriber('addout', Int, printer)

if __name__ == '__main__':
    notmain()
