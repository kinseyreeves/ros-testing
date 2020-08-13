#! /usr/bin/env python

import rospy
import rospkg
# Import the service message used by the service /trajectory_by_name
from trajectory_by_name_srv.srv import TrajByName, TrajByNameResponse
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('service_execute_traj_client')
# Wait for the service client /execute_trajectory to be running
rospy.wait_for_service('/execute_trajectory')


execute_trajectory_service_client = rospy.ServiceProxy('/execute_trajectory', ExecTraj) # Create the connection to the service
execute_trajectory_request_object = ExecTrajRequest()

rospack = rospkg.RosPack()
trajectory_file_path = rospack.get_path('unit_4_services') + "/config/init_pos.txt"
execute_trajectory_request_object.file = trajectory_file_path # Fill the variable file of this object with the desired file path
result = execute_trajectory_service_client(execute_trajectory_request_object)

print(result)