#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse

def set_twist(x, rot_z):
    twistVal = Twist()
    twistVal.linear.x = x
    twistVal.angular.z = rot_z
    return twistVal

def my_callback(request):
    endResponse = BB8CustomServiceMessageResponse()

    for i in range(0, request.repetitions):
        for k in range(0, 4):
            pub.publish(straightMov)
            rospy.sleep(request.side)
            pub.publish(stopMov)
            rospy.sleep(request.side)
            pub.publish(turnMov)
            rospy.sleep(turnTime)

    pub.publish(stopMov)

    endResponse.success = True
    return endResponse

rospy.init_node('service_server') 
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

turnTime = 3
moveSpeed = 0.25

straightMov = set_twist(moveSpeed, 0)
turnMov = set_twist(0, moveSpeed)
stopMov = set_twist(0, 0)

my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage , my_callback) # create the Service called my_service with the defined callback
rospy.spin() # maintain the service open.