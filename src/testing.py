#!/usr/bin/env python

from position import Position
from navigator import Navigator
import time

nav = Navigator()

inital_pose = Position(0.81,1.2,1)
goal = Position(2.21,0.79,1)

nav.set_initial_position(inital_pose)
time.sleep(2)
nav.go_to(goal)
