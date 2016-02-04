#!/usr/bin/env python
# license removed for brevity
import rospy
import numpy
from std_msgs.msg import String
import time
import random
from meccanoid_movements import MeccanoidMovements
import sys


class Movements():
    pub_to_robot = None
    sub_from_robot = None
    sub_kinect = None
    log = None
    to_robot_platform = "to_meccanoid"
    from_robot_platform = "from_meccanoid"
    kinect_topic = "tracking"

    traj = []               # the trajectories
    episode_length = 60     # duration, in seconds, of each episode

    # managing the kinect-driven start
    is_running = 0          # counts the number of processes, never more than 1
    kinect_state = None     # state, either calibrating or tracking


    state_stage = "pre start"   # pre start --> start --> episode
    state_start = "init"        # init --> base position
    state_traj = -1             # counter of positions in trajectory
    state_episode = None        # trajectory
    t0 = None                   # measure time inside an episode

    def __init__(self, morphology="humanoid"):
        rospy.init_node('movements')
        self.pub_to_robot = rospy.Publisher(self.to_robot_platform, String, queue_size=10)
        self.sub_from_robot = rospy.Subscriber(self.from_robot_platform, String, self.get_response)

        self.sub_kinect = rospy.Subscriber(self.kinect_topic, String, self.analyze_kinect)

        self.log = rospy.Publisher("movement_log", String, queue_size=10)


        time.sleep(1)
        mm = MeccanoidMovements(morphology)
        self.traj = mm.the_traj

        self.state_stage = "pre start"
        self.publish("init")
        rospy.spin()

    def publish(self, data):
        time.sleep(0.3)
        self.pub_to_robot.publish(data)

    def analyze_kinect(self, data):
        current_state = data.data
        if current_state == "tracking" and Movements.kinect_state == "calibrating":
            self.state_stage = "start"
            self.state_start = "base position"
            self.move_on()
        Movements.kinect_state = current_state

    def get_response(self, data):
        print(data.data)
        if "finished" in data.data:
            self.move_on()

    def send_traj(self, traj_name, pos_i = 0):
        self.publish(self.traj[traj_name][pos_i]["pos"])

    def move_on(self):
        self.log_experiment(self.state_stage)
        if self.state_stage == "start":
            self.log_experiment(self.state_start)
            if self.state_start == "init":
                self.publish("init")
                self.state_start = "base position"
                return
            if self.state_start == "base position":
                self.send_traj("base_pos")
                self.state_start = "start episode"
                return
            if self.state_start == "start episode":
                self.state_start = "base position"
                self.state_stage = "episode"
                self.state_traj = 0
                self.t0 = time.time()
                self.run_algo()
                return
        if self.state_stage == "episode":
            self.log_experiment(self.state_episode)
            if self.state_episode == None:
                #returned to base position
                self.state_traj = 0
                self.run_algo()
                return
            if self.state_traj < len(self.traj[self.state_episode]):
                # still in the loop of trajectory
                self.send_traj(self.state_episode,self.state_traj)
                self.state_traj += 1
                return
            if self.state_traj >= len(self.traj[self.state_episode]):
                # finished trajectory loop
                self.state_traj = 0
                self.run_algo()
                return

    def run_algo(self):
        if self.state_episode == None:
            if (time.time() - self.t0) < self.episode_length:
                num = random.randint(1, len(self.traj.keys())) - 1
                self.state_episode = self.traj.keys()[num]
                self.move_on()
                return
            else:
                self.log_experiment("end episode")
                self.state_stage = "start"
                return
        else: # return to base position
            self.state_episode = None
            self.send_traj("base_pos")
            return

    def log_experiment(self, comment):
        print(comment)
        self.log.publish(comment)

    def run_traj(self, t):
        # t - trajectory
        for m in t:
            if 'pos' in m:
                self.publish(m['pos'])
            if 'delay' in m:
                time.sleep(m['delay'])
        time.sleep(0.5)

if __name__ == '__main__':
    try:
        morphology = "humanoid"
        if len(sys.argv) > 1:
            morphology = sys.argv[1]
        print("Running morphology: ", morphology)
        m = Movements(morphology)

    except rospy.ROSInterruptException:
        pass
