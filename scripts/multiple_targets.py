#!/usr/bin/env python

import rospy
import actionlib
from smach import State,StateMachine
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

waypoints = [
    ['one', (2.0, 2.0), (-0.00372484207693, 0.0, 0.0, 0.999993062752)],
    ['two', (6.0, 10.0), (-0.00372484207693, 0.0, 0.0, 0.999993062752)]
]



class Waypoint(State):
    def __init__(self, position, orientation):
        State.__init__(self, outcomes=['success'])

        # Get an action client
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.client.wait_for_server()

        # Define the goal
        self.goal = MoveBaseGoal()
        self.goal.target_pose.header.frame_id = 'map'
        self.goal.target_pose.pose.position.x = position[0]
        self.goal.target_pose.pose.position.y = position[1]
        self.goal.target_pose.pose.position.z = 0.0
        self.goal.target_pose.pose.orientation.x = orientation[0]
        self.goal.target_pose.pose.orientation.y = orientation[1]
        self.goal.target_pose.pose.orientation.z = orientation[2]
        self.goal.target_pose.pose.orientation.w = orientation[3]

    def execute(self, userdata):
        self.client.send_goal(self.goal)
        self.client.wait_for_result()
        return 'success'


if __name__ == '__main__':
    rospy.init_node('patrol')

    patrol = StateMachine('success')
    with patrol:
        for i,w in enumerate(waypoints):
            StateMachine.add(w[0],
                             Waypoint(w[1], w[2]),
                             transitions={'success':waypoints[(i + 1) % \
                             len(waypoints)][0]})

    patrol.execute()