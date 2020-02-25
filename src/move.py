#!/usr/bin/env python
import roslib
import rospy
import sys
from navigation import publish_initial_pose, publish_goal


try:
    rospy.init_node('sdp-navigator')  # , log_level=roslib.msg.Log.INFO)
    # Pass arguments:Point[0],Point[1],Quaternion[2]
    myarg = rospy.myargv(argv=sys.argv)
    command = myarg[1]
    x = float(myarg[2])
    y = float(myarg[3])
    angle = float(myarg[4])

    if myarg[1] == 'pose':
        publish_initial_pose(x, y, angle)
    elif myarg[1] == 'goal':
        publish_goal(x, y, angle)
        rospy.loginfo("done")
except Exception as e:
    print("error: ", e)
