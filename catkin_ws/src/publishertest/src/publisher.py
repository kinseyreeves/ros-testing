#! /usr/bin/env python

import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
from publishertest.msg import Age

rospy.init_node('topic_publisher')
pub = rospy.Publisher('publishertest/Age', Age, queue_size=1)
rate = rospy.Rate(2)
data = Age()
data.years = 1.0
data.months = 2.0
data.days = 20.0

while not rospy.is_shutdown(): 
  pub.publish(data)
  rate.sleep()