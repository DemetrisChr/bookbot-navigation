#!/usr/bin/env python
import roslib
import rospy
import sys
from geometry_msgs.msg import *
from std_msgs.msg import Header

def gen_pose(x, y, q):
    # Latched to ensure message is sent when publisher and subscriber are ready
    pub = rospy.Publisher('initialpose', PoseWithCovarianceStamped, latch=True)
    rospy.loginfo("Setting Pose")

    p = PoseWithCovarianceStamped()
    h = Header()
    h.frame_id = 'map'
    h.stamp = rospy.Time.now()

    p.header = h

    msg = PoseWithCovariance()
    msg.pose = Pose(Point(x, y, 0), Quaternion(0, 0, q, 1))
    msg.covariance = [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853891945200942]
    p.pose = msg

    rospy.Rate(1).sleep()
    pub.publish(p)

def publish_nav_goal(x, y, q):
    # Currently publishes a set position as the goal
    publisher = rospy.Publisher('move_base_simple/goal', PoseStamped, latch=True)
    rospy.loginfo("Sending Navigation Goal")

    p = PoseStamped()
    h = Header()
    h.frame_id = 'map'
    h.stamp = rospy.Time.now()


    p.header = h
    p.pose = Pose(Point(x, y, 0), Quaternion(0, 0, q, 1))

    rospy.Rate(1).sleep()
    publisher.publish(p)

if __name__ == '__main__':
    try:
        rospy.init_node('sdp-navigator'); #, log_level=roslib.msg.Log.INFO)

        # Pass arguments:Point[0],Point[1],Quaternion[2]
        myarg = rospy.myargv(argv=sys.argv)
        command = myarg[1]
        x = float(myarg[2])
        y = float(myarg[3])
        angle = float(myarg[4])

        if myarg[1] == 'pose':
            gen_pose(x, y, angle)
        elif myarg[1] == 'goal':
            publish_nav_goal(x, y, angle)
        rospy.loginfo("done")
    except Exception as e:
        print("error: ", e)
