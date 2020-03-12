#!/usr/bin/env python
import roslib
import rospy
import sys
from navigator import Navigator
from position import Position

try:
    rospy.init_node('sdp_navigator')
    nav = Navigator()
    
    # Pass arguments:Point[0],Point[1],Quaternion[2]
    myarg = rospy.myargv(argv=sys.argv)
    command = myarg[1]
    x = float(myarg[2])
    y = float(myarg[3])
    angle = float(myarg[4])

    position = Position(x, y, angle)

    if myarg[1] == 'pose':
        nav.set_initial_position(position)
    elif myarg[1] == 'goal':
        nav.go_to(position)
    
    rospy.loginfo("done")
except Exception as e:
    print("error: ", e)
