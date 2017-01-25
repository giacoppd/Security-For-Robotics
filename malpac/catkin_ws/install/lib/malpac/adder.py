#!/usr/bin/env python
import rospy
from std_msgs.msg import Int

def notmain():
    rospy.init_node('adder', anonymous=True)
    pub = rospy.Publisher('addout', Int, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        cur_int = cur_int+1
        pub.publish(cur_int)
        rate.sleep()

if __name__ == '__main__':
    notmain()
