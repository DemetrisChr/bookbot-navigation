#!/usr/bin/env python

import roslib
import rospy
from nav_msgs.msg import Odometry
from navigation import publish_initial_pose, publish_goal

goals = [{"x":-0.25, "y":-1.3, "q": 0}, {"x":3, "y":0.3, "q": -0.6}]
current_goal = goals.pop(0)

def approxEq(pose1, pose2):
    dp = 2

    x1 = round(pose1["x"], dp)
    x2 = round(pose2["x"], dp)

    y1 = round(pose1["y"], dp)
    y2 = round(pose2["y"], dp)

    q1 = round(pose1["q"], dp)
    q2 = round(pose2["q"], dp)

    return (x1 == x2) and (y1 == y2) and (q1 == q2)


def callback(msg):
    global goals, current_goal
    position = msg.pose.pose.position
    angle = msg.pose.pose.orientation.z
    current_pose = {"x": float(position.x), "y": float(position.y), "q": float(angle)}
    print(current_goal)
    if(approxEq(current_pose, current_goal)):
        if(len(goals) > 0):
            current_goal = goals.pop(0)
            
            publish_goal(**current_goal)
        else:
            exit()


rospy.init_node('demo2_node')

initial_pose = {"x":0.8, "y":1.2, "q": 0}


publish_initial_pose(**initial_pose)
publish_goal(**current_goal)

odom_sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()