import roslib
import rospy
from geometry_msgs.msg import *
from actionlib_msgs.msg import GoalStatusArray
from std_msgs.msg import Header
from position import Position
from move_base_status import MoveBaseStatus

class Navigator():
    def __init__(self):
        self._queue = []
        self._state = "idle"
        self._current_goal = None
        self._goal_index = 1

        rospy.Subscriber('/move_base/status', GoalStatusArray, self._update_loop)

    def _update_loop(self, move_base_status_msg):
        move_base_status = MoveBaseStatus(move_base_status_msg)
        goalreached = False
        if (len(msg.status_list) > 0):
            print(msg.status_list[-1])
            msg_goal_id = msg.status_list[-1].goal_id.id.split("-")[1]
            print(msg_goal_id)
            if(msg.status_list[-1].status == 3 and msg_goal_id == str(self._goal_index)):
                goalreached = True
            else:
                goalreached = False

        if(goalreached):
            if(len(self._queue) > 0):
                print("Performing next move")

                self._current_goal = self._queue.pop(0)
                publish_goal(self._current_goal)
                self._goal_index += 1
            else:
                print("Goal reached but got no where to go")

    def add_to_queue(self, positions):
        self._queue += positions

    def set_initial_position(self, position):
        message = position.generate_stamped_message(True)
        
        rospy.loginfo("Setting Pose")

        self._publish('initialpose', PoseWithCovarianceStamped, message)



    def _publish(self, topic, publisher, message):
        # Latched to ensure message is sent when publisher and subscriber are ready
        pub = rospy.Publisher(topic, publisher, latch=True)
        rospy.Rate(1).sleep()
        pub.publish(message)

    def publish_goal(position):
        # Currently publishes a set position as the goal
        publisher = rospy.Publisher('move_base_simple/goal', PoseStamped, latch=True)
        rospy.loginfo("Sending Navigation Goal")

        message = position.generate_stamped_message(False)

        rospy.Rate(1).sleep()
        publisher.publish(message)