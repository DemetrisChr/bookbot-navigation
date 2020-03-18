#!/usr/bin/env python
import roslib
import rospy
from position import Position
from navigator import Navigator
import time

rospy.init_node('sdp_navigator')

nav = Navigator()

inital_pose = Position(0.88, 1.14, 0, 1)
goal = Position(2.9, -1.4, 0.95, 0)

nav.set_initial_position(inital_pose)
#
time.sleep(2)
nav.go_to(goal)
