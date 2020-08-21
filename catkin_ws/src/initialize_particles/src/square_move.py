#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty, EmptyRequest # Import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import PoseWithCovarianceStamped, Pose


def disperse():
    rospy.wait_for_service('/global_localization')

    client = rospy.ServiceProxy('/global_localization', Empty)

    req_object = EmptyRequest()
    result = client(req_object)
    print(result)
    print("hello")

class SquareMove:
    """
    Move the robot in a square to localize its position
    """

    def __init__(self):
        
        self.pub_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.sub_pose = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, self.sub_pose_callback)
        self.vel_value = Twist()
        self.pose = None
        self.covariance = 1
        self.covariance_arr = []
        self.disperse()
        self.rate = rospy.Rate(5)
        self.run()

    def run(self):
        while self.covariance > 0.65:
            self.disperse()
            self.square_move()
            self.covariance = self.calc_covariance()

        print("calibrated..")
        self.shutdown()

    def shutdown(self):
        pass

    def calc_covariance(self):
        if(len(self.covariance_arr)>0):
            cov_x = self.covariance_arr[0]
            cov_y = self.covariance_arr[7]
            cov_z = self.covariance_arr[35]
            cov = (cov_x + cov_y + cov_z) / 3
        else:
            cov = 1

        return cov

    def disperse(self):
        rospy.wait_for_service('/global_localization')
        client = rospy.ServiceProxy('/global_localization', Empty)
        req_object = EmptyRequest()
        result = client(req_object)

    def sub_pose_callback(self, msg):
        print("getting pose")
        self.pose = msg.pose
        self.covariance_arr = msg.pose.covariance

    def square_move(self):
        def move_forward():
            print("moving foward")
            i= 0
            while i < 10:
                i+=1
                self.vel_value.linear.x = 0.8
                self.vel_value.angular.z = 0
                self.pub_vel.publish(self.vel_value)
                self.rate.sleep()
            
        def turn_left(linear_vel = 0.0, angular_vel=0.8):
            print("moving left")
            i= 0
            while i < 10:
                i+=1
                self.vel_value.linear.x = linear_vel
                self.vel_value.angular.z = angular_vel
                self.pub_vel.publish(self.vel_value)
                self.rate.sleep()
        
        for i in range(0,4):
            move_forward()
            turn_left()
        

        return


    def print_covar(self):
        pass


if __name__ == '__main__':
    rospy.init_node("SquareMove")
    a = SquareMove()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "done"