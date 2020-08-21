#! /usr/bin/env python


import rospy
from std_srvs.srv import Empty, EmptyRequest # Import the service message python classes generated from Empty.srv.



rospy.wait_for_service('/global_localization')

client = rospy.ServiceProxy('/global_localization', Empty)

req_object = EmptyRequest()
result = client(req_object)
print(result)
print("hello")