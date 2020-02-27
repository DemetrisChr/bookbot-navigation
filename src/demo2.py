#!/usr/bin/env python

import roslib
import rospy
from nav_msgs.msg import Odometry
from move_base_msgs.msg import MoveBaseActionFeedback
from navigation import publish_initial_pose, publish_goal

goals = [{"x":3.21, "y":-0.38, "q": -0.71}, {"x":-0.04, "y":-0.67, "q": -0.71}, {"x":0.8, "y":1.2, "q": 0}]
current_goal = goals.pop(0)

def approxEq(pose1, pose2):
    dp = 1

    x1 = round(pose1["x"], dp)
    x2 = round(pose2["x"], dp)

    y1 = round(pose1["y"], dp)
    y2 = round(pose2["y"], dp)

    q1 = round(pose1["q"], dp)
    q2 = round(pose2["q"], dp)
    #print("Aprox x", str((x1 == x2)))
    # print(x1)
    # print(x2)
    #print("Aprox y", str((y1 == y2)))
    # print(y1)
    # print(y2)
    #print("Aprox q", str((q1 == q2)))
    # print(q1)
    # print(q2)
    return (x1 == x2) and (y1 == y2) and (q1 == q2)


def callback(msg):
    global goals, current_goal
    position = msg.feedback.base_position.pose.position 
    angle = msg.feedback.base_position.pose.orientation.z
    current_pose = {"x": float(position.x), "y": float(position.y), "q": float(angle)}
    #print(current_goal)
    if(approxEq(current_pose, current_goal)):
        if(len(goals) > 0):
            print("Reached goal, waiting then moving on...")
            #rospy.Rate(2000).sleep()
            current_goal = goals.pop(0)
            publish_goal(**current_goal)
        else:
            exit()


rospy.init_node('demo2_node')

initial_pose = {"x":0.8, "y":1.2, "q": 0}


publish_initial_pose(**initial_pose)
publish_goal(**current_goal)

odom_sub = rospy.Subscriber('/move_base/feedback', MoveBaseActionFeedback, callback)
rospy.spin()