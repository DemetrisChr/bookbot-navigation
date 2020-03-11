import roslib
import rospy
from geometry_msgs.msg import *
from std_msgs.msg import Header
from position import Position

def publish_initial_pose(position):
    # Latched to ensure message is sent when publisher and subscriber are ready
    pub = rospy.Publisher('initialpose', PoseWithCovarianceStamped, latch=True)
    rospy.loginfo("Setting Pose")

    message = position.generate_stamped_message(True)

    rospy.Rate(1).sleep()
    pub.publish(message)

def publish_goal(position):
    # Currently publishes a set position as the goal
    publisher = rospy.Publisher('move_base_simple/goal', PoseStamped, latch=True)
    rospy.loginfo("Sending Navigation Goal")

    message = position.generate_stamped_message(False)

    rospy.Rate(1).sleep()
    publisher.publish(message)