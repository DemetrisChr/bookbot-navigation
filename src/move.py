#!/usr/bin/env python
import roslib
import rospy
from geometry_msgs.msg import *

def gen_pose():
    pub = rospy.Publisher('initialpose', PoseWithCovarianceStamped)
    rospy.init_node('initial_pose'); #, log_level=roslib.msg.Log.INFO)
    rospy.loginfo("Setting Pose")

    p   = PoseWithCovarianceStamped();
    msg = PoseWithCovariance();
    msg.pose = Pose(Point(-0.767, -0.953, 0.000), Quaternion(0.000, 0.000, -0.0149, 0.9999));
    msg.covariance = [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853891945200942];
    p.pose = msg;
    pub.publish(p);

def publish_nav_goal():
    #Currently publishes a set position as the goal
    publisher = rospy.Publisher('move_base_simple/goal', PoseStamped)
    p = PoseStamped()
    p.pose = Pose(Point(-0.767, -0.953, 0.000), Quaternion(0.000, 0.000, -0.0149, 0.9999))
    publisher.publish(p)

if __name__ == '__main__':
    try:
        gen_pose()
        publish_nav_goal()
        rospy.loginfo("done")
    except Exception, e:
        print "error: ", e
