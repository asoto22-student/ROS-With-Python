#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist

def my_callback(request):
    circleMov = Twist()
    circleMov.linear.x = 0.125
    circleMov.angular.z = 0.125

    pub.publish(circleMov)

    print "bb8 is now moving in a circle!"
    return EmptyResponse()

rospy.init_node('service_server')
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
my_service = rospy.Service('/move_bb8_in_circle', Empty , my_callback) # create the Service called my_service with the defined callback
rospy.spin() # maintain the service open.