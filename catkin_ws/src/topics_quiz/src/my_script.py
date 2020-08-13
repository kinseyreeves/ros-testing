#! /usr/bin/env python

import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

rospy.init_node('quiz_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

x = 0
z = 0
value = Twist()

def callback(msg):
    global value

    value.linear.x = 0.5
    value.linear.z = 0.5
    value.angular.z = 0
    value.angular.x = 0

    forward = msg.ranges[360]
    f_left = msg.ranges[420]
    f_right = msg.ranges[300]
    left = msg.ranges[719]
    right = msg.ranges[0]

    if(forward < 1 or right < 1):
        value.linear.x = 0
        value.linear.z = 0
        value.angular.x = 0.7
        value.angular.z = 0.7

sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)   # Create a Subscriber object that will listen to the /counter
r = rospy.Rate(2)


while not rospy.is_shutdown():
    print(value.linear.x)
    pub.publish(value)
    r.sleep()
