#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from unit_4_services.srv import CustomCircleMsg, CustomCircleMsgResponse

def my_callback(request):
    endResponse = CustomCircleMsgResponse()

    pub.publish(stopMov)
    print "bb8 is now moving in a circle!"
    rospy.sleep(0.1)

    pub.publish(straightMov)
    rospy.sleep(request.duration)

    pub.publish(stopMov)
    print "bb8 stopped moving in a circle!"

    endResponse.success = True

    return endResponse

rospy.init_node('service_server') 
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

straightMov = Twist()
straightMov.linear.x = 0.125
straightMov.angular.z = 0.125

stopMov = Twist()
stopMov.linear.x = 0
stopMov.angular.z = 0

my_service = rospy.Service('/move_bb8_in_circle_custom', CustomCircleMsg , my_callback) # create the Service called my_service with the defined callback
rospy.spin() # maintain the service open.