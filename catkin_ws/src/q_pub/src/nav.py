#! /usr/bin/env python

import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def callback(msg):                                    # Define a function called 'callback' that receives a parameter 
                                                      # named 'msg'
    print(msg)
    #print(msg)

rospy.init_node('q_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)   # Create a Subscriber object that will listen to the /counter
        
rate = rospy.Rate(2)
data = Twist()
data.linear.x = 0.5
data.linear.z = 0.5

while not rospy.is_shutdown(): 
  pub.publish(data)
  rate.sleep()