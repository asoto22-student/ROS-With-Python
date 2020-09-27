#! /usr/bin/env python
import rospy
import actionlib
# from actionlib.msg import TestActionFeedback, TestActionResult, TestAction
# from geometry_msgs.msg import Twist
from actions_quiz.msg import CustomActionMsgFeedback, CustomActionMsgResult, CustomActionMsg
from std_msgs.msg import Empty

class CustomActionClass(object):
  _feedback   = TestActionFeedback()
  _result     = TestActionResult()
  _pubTakoff  = rospy.Publisher("/drone/takeoff", Empty, queue_size=10)
  _pubLand  = rospy.Publisher("/drone/land", Empty, queue_size=10)

  def __init__(self):
    self._as = actionlib.SimpleActionServer("/action_custom_msg_as", TestAction, self.goal_callback, False)
    self._as.start()
    
  def goal_callback(self, goal):
    success = True

    # publish info to the console for the user
    if (goal == 'TAKEOFF'):
        self._pubTakoff.publish(Empty())
        _feedback.feedback = "TAKEOFF"
    elif (goal == 'LAND'):
        self._pubLand.publish(Empty())
        _feedback.feedback = "LAND"
    else:
        rospy.loginfo('The goal has been cancelled/preempted')
        self._as.set_preempted()
        success = False

    if success:
        rospy.loginfo('Succeeded in creating the square')
        self._as.set_succeeded(self._feedback)
      
if __name__ == '__main__':
  rospy.init_node('action_custom_msg_as')
  CustomActionClass()
  rospy.spin()