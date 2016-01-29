#!/usr/bin/env python
# license removed for brevity
import rospy
import numpy
from std_msgs.msg import String
import time
import random
from meccanoid_movements import MeccanoidMovements


class Movements():
    pub = None
    sub = None
    log = None
    robot_platform = "to_meccanoid"
    kinect_topic = "tracking"

    traj = []               # the trajectories
    base_pos = []
    base_traj = []
    episode_length = 60     # duration, in seconds, of each episode

    # managing the kinect-driven start
    is_running = 0          # counts the number of processes, never more than 1
    kinect_state = None     # state, either calibrating or tracking


    def __init__(self):
        rospy.init_node('movements')
        self.pub = rospy.Publisher(self.robot_platform, String, queue_size=10)
        self.log = rospy.Publisher("movement_log", String, queue_size=10)
        self.sub = rospy.Subscriber(self.kinect_topic, String, self.analyze_kinect)
        time.sleep(1)
        mm = MeccanoidMovements()
        self.traj = mm.the_traj
        self.base_pos = mm.the_base_pos
        self.base_traj = mm.the_base_traj

        rospy.spin()

    def publish(self, data):
        self.pub.publish(data)
        time.sleep(1.5)

    def analyze_kinect(self, data):
        current_state = data.data
        if current_state == "tracking" and Movements.kinect_state == "calibrating":
            print("kinect")
            self.start_episode()
        Movements.kinect_state = current_state

    def start_episode(self):
        self.log_experiment("start episode")
        Movements.is_running += 1
        self.log_experiment("base position")
        self.run_traj(self.base_pos)
        self.run()

    def run(self):
        # set to initial position
        self.log_experiment("base trajectory")
        self.run_traj(self.base_traj)

        self.log_experiment("base position")
        self.run_traj(self.base_pos)

        if len(self.traj) > 0:
            k = 0
            t0 = time.time()
            dt = time.time() - t0
            while dt < self.episode_length and Movements.is_running == 1:
                # generate a random motion
                num = random.randint(1, len(self.traj.keys())) - 1

                self.log_experiment(self.traj.keys()[num])
                self.run_traj(self.traj[self.traj.keys()[num]])

                self.log_experiment("base position")
                self.run_traj(self.base_pos)
                dt = time.time() - t0

                k+=1
            Movements.is_running -= 1
        self.end_episode()

    def end_episode(self):
        self.log_experiment("end episode")
        kinect_state = None

    def log_experiment(self, comment):
        print(comment)
        self.log.publish(comment)

    def run_traj(self, t):
        # t - trajectory
        for m in t:
            if Movements.is_running == 1:
                if 'pos' in m:
                    self.publish(m['pos'])
                if 'delay' in m:
                    time.sleep(m['delay'])

if __name__ == '__main__':
    try:
        m = Movements()
#        m.start_episode()

    except rospy.ROSInterruptException:
        pass