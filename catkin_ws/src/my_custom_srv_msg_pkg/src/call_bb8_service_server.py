#! /usr/bin/env python
#TODO call the service
import rospy
# Import the service message used by the service /trajectory_by_name
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessageRequest, MyCustomServiceMessage # you import the service message python classes 
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('service_client_bb8')
# Wait for the service client /execute_trajectory to be running
rospy.wait_for_service('/move_bb8_in_circle_custom')

move_bb8_client = rospy.ServiceProxy('/move_bb8_in_circle_custom', MyCustomServiceMessage)

move_bb8_in_circle_request_object = MyCustomServiceMessageRequest()
move_bb8_in_circle_request_object.duration = 5
result = move_bb8_client(move_bb8_in_circle_request_object)