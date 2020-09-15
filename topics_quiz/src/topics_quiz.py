#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class TopicQuiz:
    def __init__(self):
        self.frontDist = 0.0
        self.leftDist = 0.0
        self.rightDist = 0.0

        rospy.init_node("topics_quiz_node")
        self.pub = rospy.Publisher("cmd_vel", Twist, queue_size = 10)
        self.sub = rospy.Subscriber("/kobuki/laser/scan", LaserScan, self.ParseMessage)

        self.loopRate = rospy.Rate(100)

    def ParseMessage(self, msg):
        self.frontDist = msg.ranges[360]
        self.leftDist = msg.ranges[719]
        self.rightDist = msg.ranges[0]

    def loop(self):
        forward = Twist()
        leftTurn = Twist()
        rightTurn = Twist()

        forward.linear.x = 0.25
        rightTurn.angular.z = -0.25
        leftTurn.angular.z = 0.25

        while(not rospy.is_shutdown()):
            if (self.frontDist > 1):
                self.pub.publish(forward)
            else:
                self.pub.publish(leftTurn)
            if (self.rightDist < 1):
                self.pub.publish(leftTurn)
            if (self.leftDist < 1):
                self.pub.publish(rightTurn)

tq = TopicQuiz()
tq.loop()
rospy.spin()