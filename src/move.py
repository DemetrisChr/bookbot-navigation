#!/usr/bin/env python
import roslib
import rospy
from geometry_msgs.msg import *
from std_msgs.msg import Header

def gen_pose():
    # Latched to ensure message is sent when publisher and subscriber are ready
    pub = rospy.Publisher('initialpose', PoseWithCovarianceStamped, latch=True)
   # rospy.init_node('initial_pose'); #, log_level=roslib.msg.Log.INFO)
   # rospy.loginfo("Setting Pose")

    p   = PoseWithCovarianceStamped()
    h = Header()
    h.frame_id = 'map'
    h.stamp = rospy.Time.now()


    p.header = h

    msg = PoseWithCovariance()
    msg.pose = Pose(Point(0.805000007153, 1.19999969006, 0), Quaternion(0, 0, 0, 1))
    msg.covariance = [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853891945200942]
    p.pose = msg

    rospy.Rate(1).sleep()
    pub.publish(p)

def publish_nav_goal():
    #Currently publishes a set position as the goal
    publisher = rospy.Publisher('move_base_simple/goal', PoseStamped, latch=True)
    p = PoseStamped()
    h = Header()
    h.frame_id = 'map'
    h.stamp = rospy.Time.now()


    p.header = h
    p.pose = Pose(Point(-0.247143253684, -1.25660061836, 0.000), Quaternion(0.000, 0.000, -0.0149, 0.9999))
    
    rospy.Rate(1).sleep()
    publisher.publish(p)

if __name__ == '__main__':
    try:
        rospy.init_node('initial_pose'); #, log_level=roslib.msg.Log.INFO)
        rospy.loginfo("Setting Pose")

        gen_pose()
        #publish_nav_goal()
        rospy.loginfo("done")
    except Exception as e:
        print("error: ", e)
