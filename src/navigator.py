import roslib
import rospy
from geometry_msgs.msg import *
from actionlib_msgs.msg import GoalStatusArray
from std_msgs.msg import Header
from position import Position
from move_base_status import MoveBaseStatus
# 13cm
class Navigator():
    def __init__(self):
        self._goal = None
        self._goal_callback = None
        self._goal_index = 1

        rospy.Subscriber('/move_base/status', GoalStatusArray, self._update_loop)

    def _update_loop(self, move_base_status_msg):
        move_base_status = MoveBaseStatus(move_base_status_msg)
        
        goal_reached = (move_base_status.status == 3) and (move_base_status.goal_id == self._goal_index)
        if goal_reached:
            rospy.loginfo("Arrived at goal")
            self._goal = None
            self._goal_index += 1
            if self._goal_callback is not None:
                self._goal_callback()
                self._goal_callback = None

    def go_to(self, position, callback=None):
        self._goal = position
        self._goal_callback = callback

        message = position.generate_stamped_message(False)
        rospy.loginfo("Setting Goal")
        self._publish('move_base_simple/goal', PoseStamped, message)

    def set_initial_position(self, position):
        message = position.generate_stamped_message(True)
        rospy.loginfo("Setting Pose")
        self._publish('initialpose', PoseWithCovarianceStamped, message)


    def _publish(self, topic, publisher, message):
        # Latched to ensure message is sent when publisher and subscriber are ready
        pub = rospy.Publisher(topic, publisher, latch=True)
        rospy.Rate(1).sleep()
        pub.publish(message)