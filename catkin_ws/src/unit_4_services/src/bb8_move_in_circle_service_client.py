#! /usr/bin/env python
#TODO call the service
import rospy
import rospkg
# Import the service message used by the service /trajectory_by_name
from trajectory_by_name_srv.srv import TrajByName, TrajByNameResponse
from std_srvs.srv import Empty, EmptyRequest
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('service_client_bb8')
# Wait for the service client /execute_trajectory to be running
rospy.wait_for_service('/move_bb8_in_circle')

move_bb8_client = rospy.ServiceProxy('/move_bb8_in_circle', Empty)

move_bb8_in_circle_request_object = EmptyRequest()
result = move_bb8_client(move_bb8_in_circle_request_object)