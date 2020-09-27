#! /usr/bin/env python
import rospy
import time
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

nImage = 1

# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received
def feedback_callback(feedback):
    global nImage
    print('[Feedback] image n.%d received'%nImage)
    nImage += 1

# initializes the action client node
rospy.init_node('drone_action_client')

# create the connection to the action server
client = actionlib.SimpleActionClient('/ardrone_action_server', ArdroneAction)
# waits until the action server is up and running
client.wait_for_server()

pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
pubStart = rospy.Publisher("/drone/takeoff", Empty, queue_size=10)
pubEnd = rospy.Publisher("/drone/land", Empty, queue_size=10)

# creates a goal to send to the action server
goal = ArdroneGoal()
goal.nseconds = 10 # indicates, take pictures along 10 seconds

# sends the goal to the action server, specifying which feedback function
# to call when feedback received
client.send_goal(goal, feedback_cb=feedback_callback)

# Uncomment these lines to test goal preemption:
#time.sleep(3.0)
#client.cancel_goal()  # would cancel the goal 3 seconds after starting

# wait until the result is obtained
# you can do other stuff here instead of waiting
# and check for status from time to time 
# status = client.get_state()
# check the client API link below for more info

# client.wait_for_result()
moveLeft = Twist()
moveLeft.linear.z = 1

stopMove = Twist()
stopMove.linear.y = 0
rate = rospy.Rate(1)

status = client.get_state()
emptyVal = Empty()

pubStart.publish(emptyVal)

while (status < 2):
    print("Should be moving ups?")
    pub.publish(moveLeft)
    rate.sleep()
    status = client.get_state()

pub.publish(stopMove)
pubEnd.publish(emptyVal)

print('[Result] State: %d'%(client.get_state()))