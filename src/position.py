#!/usr/bin/env python

import roslib
import rospy
from geometry_msgs.msg import *
from std_msgs.msg import Header

class Position():
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def generate_stamped_message(self, covariance=False):
        h = Header()
        h.frame_id = 'map'
        h.stamp = rospy.Time.now()

        p = PoseStamped()
        msg = Pose(Point(self.x, self.y, 0), Quaternion(0, 0, self.angle, 1))
        
        if covariance:
            p = PoseWithCovarianceStamped()
            msg = PoseWithCovariance()
            msg.pose = Pose(Point(self.x, self.y, 0), Quaternion(0, 0, self.angle, 1))
            msg.covariance = [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853891945200942]

        p.header = h
        p.pose = msg

        return p