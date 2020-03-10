#!/usr/bin/env python

import roslib
import rospy
import time
from nav_msgs.msg import Odometry
from actionlib_msgs.msg import GoalStatusArray
from navigation import publish_initial_pose, publish_goal
from datetime import datetime

goals = [{"x":3.21, "y":-0.38, "q": -0.71}, {"x":-0.04, "y":-0.67, "q": -0.71}, {"x":0.8, "y":1.2, "q": 0}]
current_goal = goals.pop(0)

time_since_goal_reached = time.time()


def callback(msg):
    global goals, current_goal, time_since_goal_reached
    #print(current_goal)

    goalreached = False
    #print(msg.status_list)
    if (len(msg.status_list) > 0 ):
        goalreached = msg.status_list[0].text == "Goal reached."

        if goalreached:
            now = time.time()
            time_since = now - time_since_goal_reached
            if(time_since < 8):
                goalreached = False
            else:
                time_since_goal_reached = time.time()

    if(goalreached):
        if(len(goals) > 0):
            print("Performing next move")
            
            current_goal = goals.pop(0)
            publish_goal(**current_goal)
        else:
            print("Goal reached but got no where to go")

rospy.init_node('demo2_node')

initial_pose = {"x":0.8, "y":1.2, "q": 0}


publish_initial_pose(**initial_pose)
publish_goal(**current_goal)

odom_sub = rospy.Subscriber('/move_base/status', GoalStatusArray, callback)
rospy.spin()