#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest
import sys

small_square = BB8CustomServiceMessageRequest()
small_square.side = 1.7
small_square.repetitions = 2

big_square = BB8CustomServiceMessageRequest()
big_square.side = 2.5
big_square.repetitions = 1

rospy.init_node('service_client')
rospy.wait_for_service('/move_bb8_in_square_custom')
move_bb8_service = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)

move_bb8_service(small_square)
move_bb8_service(big_square)