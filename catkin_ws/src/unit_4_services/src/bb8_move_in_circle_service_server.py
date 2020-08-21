#! /usr/bin/env python
#Service server, client connects to this
import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
value = Twist()

def my_callback(request):
    global value
    print "My_callback has been called"
    
    value.linear.x = 0.5
    value.linear.z = 0.5
    value.angular.z = .5
    value.angular.x = .5
    pub.publish(value)
    
    return EmptyResponse() # the service Response class, in this case EmptyResponse

    #return MyServiceResponse(len(request.words.split())) 

rospy.init_node('service_server')
my_service = rospy.Service('/move_bb8_in_circle', Empty , my_callback) # create the Service called my_service with the defined callback
pub.publish(value)
print("here")
rospy.spin() 