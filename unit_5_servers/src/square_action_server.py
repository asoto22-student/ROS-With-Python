#! /usr/bin/env python
import rospy
import actionlib
#from actionlib_tutorials.msg import FibonacciFeedback, FibonacciResult, FibonacciAction
from actionlib.msg import TestActionFeedback, TestActionResult, TestAction
from geometry_msgs.msg import Twist

class SquareClass(object):
  _feedback   = TestActionFeedback()
  _result     = TestActionResult()
  _motionVect = Twist()
  _stopVect   = Twist()

  def __init__(self):
    self._as = actionlib.SimpleActionServer("square_as", TestAction, self.goal_callback, False)
    self._as.start()
    self._pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    self._motionVect.linear.x = 0
    self._motionVect.linear.y = 0
    self._stopVect.linear.x = 0
    self._stopVect.linear.y = 0
    
  def goal_callback(self, goal):
    r = rospy.Rate(goal.goal)
    success = True
        
    # publish info to the console for the user
    rospy.loginfo('"square_as": Executing, creating square with a length of %i units', goal.goal)

    for i in range(0, 4):
        if (i % 2 == 1):
            self._motionVect.linear.x = 0.25 * (i - 2)
            self._motionVect.linear.y = 0
        else:
            self._motionVect.linear.x = 0
            self._motionVect.linear.y = 0.25 * (i - 1)

        self._pub.publish(self._motionVect)
        rospy.sleep(goal.goal)
        self._feedback.feedback = i
        self._pub.publish(self._stopVect)
        rospy.sleep(1)

        if self._as.is_preempt_requested():
            rospy.loginfo('The goal has been cancelled/preempted')
            self._as.set_preempted()
            success = False
            break

    if success:
        self._result.result = self._feedback.feedback * goal.goal * 2
        rospy.loginfo('Succeeded in creating the square')
        self._as.set_succeeded(self._result)
      
if __name__ == '__main__':
  rospy.init_node('square_action_client')
  rospy.loginfo('Square Action Starting!')
  SquareClass()
  rospy.spin()