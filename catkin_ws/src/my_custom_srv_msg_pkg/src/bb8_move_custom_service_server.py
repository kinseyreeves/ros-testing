#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
value = Twist()

def my_callback(request):
    global value
    print "Request Data==> duration="+str(request.duration)

    value.linear.x = 0.5
    value.linear.z = 0.5
    value.angular.z = .5
    value.angular.x = .5
    pub.publish(value)
    rospy.sleep(request.duration)
    value.linear.x = 0
    value.linear.z = 0
    value.angular.z = 0
    value.angular.x = 0
    pub.publish(value)
    my_response = MyCustomServiceMessageResponse()
    my_response.success = True
    return my_response # the service Response class, in this case EmptyResponse

    #return MyServiceResponse(len(request.words.split())) 

rospy.init_node('custom_service_server')
my_service = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage , my_callback) # create the Service called my_service with the defined callback
pub.publish(value)

rospy.spin() 