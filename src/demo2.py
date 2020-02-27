#!/usr/bin/env python

import roslib
import rospy
from nav_msgs.msg import Odometry
from anctionlib_msg import GoalStatusArray
from navigation import publish_initial_pose, publish_goal

goals = [{"x":3.21, "y":-0.38, "q": -0.71}, {"x":-0.04, "y":-0.67, "q": -0.71}, {"x":0.8, "y":1.2, "q": 0}]
current_goal = goals.pop(0)


def callback(msg):
    global goals, current_goal
    #print(current_goal)

    goalreached = False
    if (len(msg.status_list) > 0 ):
        goalreached = msg.status_list.text == "Goal reached." 

    if(goalreached):
        if(len(goals) > 0):
            print("Reached goal, waiting then moving on...")
            rospy.Rate(2000).sleep()
            current_goal = goals.pop(0)
            publish_goal(**current_goal)
        else:
            exit()


rospy.init_node('demo2_node')

initial_pose = {"x":0.8, "y":1.2, "q": 0}


publish_initial_pose(**initial_pose)
publish_goal(**current_goal)

odom_sub = rospy.Subscriber('/move_base/status', GoalStatusArray, callback)
rospy.spin()