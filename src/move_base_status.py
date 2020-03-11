class MoveBaseStatus():
    # Used to extract last status in a move base status list

    def __init__(self, status_msg):
        self.status = None
        self.goal_id = None
        if (len(status_msg.status_list) > 0 ):
            self.status = int(status_msg.status_list[-1].status)
            self.goal_id = int(status_msg.status_list[-1].goal_id.id.split("-")[1])