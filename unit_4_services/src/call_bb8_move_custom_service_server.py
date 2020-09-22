#! /usr/bin/env python

import rospy
from unit_4_services.srv import CustomCircleMsg, CustomCircleMsgRequest
import sys

move_bb8_object = CustomCircleMsgRequest()
move_bb8_object.duration = 5

rospy.init_node('service_client')
rospy.wait_for_service('/move_bb8_in_circle_custom')
move_bb8_service = rospy.ServiceProxy('/move_bb8_in_circle_custom', CustomCircleMsg)

result = move_bb8_service(move_bb8_object)
print "Was it sucessful?: " + str(result.success)