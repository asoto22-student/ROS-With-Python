#! /usr/bin/env python
import rospy
import actionlib
# from actionlib.msg import TestActionFeedback, TestActionResult, TestAction
# from geometry_msgs.msg import Twist
from actions_quiz.msg import CustomActionMsgFeedback, CustomActionMsgResult, CustomActionMsgAction
from std_msgs.msg import Empty

class CustomActionClass(object):
  _feedback   = CustomActionMsgFeedback()
  _result     = CustomActionMsgResult()
  _pubTakoff  = rospy.Publisher("/drone/takeoff", Empty, queue_size=10)
  _pubLand  = rospy.Publisher("/drone/land", Empty, queue_size=10)

  def __init__(self):
    self._as = actionlib.SimpleActionServer("/action_custom_msg_as", CustomActionMsgAction, self.goal_callback, False)
    self._as.start()
    
  def goal_callback(self, goal):
    success = True

    # publish info to the console for the user
    if (goal.goal == 'TAKEOFF'):
        rospy.loginfo("Taking off!")
        self._pubTakoff.publish(Empty())
        self._feedback.feedback = "TAKEOFF"
    elif (goal.goal == 'LAND'):
        rospy.loginfo("Landing!")
        self._pubLand.publish(Empty())
        self._feedback.feedback = "LAND"
    else:
        rospy.loginfo('The goal has been cancelled/preempted')
        self._as.set_preempted()
        success = False

    self._as.publish_feedback(self._feedback)

    if success:
        rospy.loginfo('Success!')
        self._as.set_succeeded(self._feedback)
      
if __name__ == '__main__':
  rospy.init_node('action_custom_msg_as')
  CustomActionClass()
  rospy.spin()