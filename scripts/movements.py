#!/usr/bin/env python
# license removed for brevity
import rospy
import numpy
from std_msgs.msg import String
import time
import random


class Movements():
    pub = None
    sub = None
    robot_platform = "to_meccanoid"
    kinect_topic = "tracking"

    traj = []               # the trajectories
    episode_length = 15     # duration, in seconds, of each episode

    # managing the kinect-driven start
    is_running = 0          # counts the number of processes, never more than 1
    kinect_state = None     # state, either calibrating or tracking

    base_pos = [{'pos': '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0', 'delay': 1}]
    base_traj = [{'pos': '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0', 'delay': 1}]


    def __init__(self):
        rospy.init_node('movements')
        self.pub = rospy.Publisher(self.robot_platform, String, queue_size=10)
        self.sub = rospy.Subscriber(self.kinect_topic, String, self.analyze_kinect)
        self.init_traj()

    def publish(self, data):
        self.pub.publish(data)

    def analyze_kinect(self, data):
        current_state = data.data
        if current_state == "tracking" and Movements.kinect_state == "calibrating":
            print("kinect", Movements.is_running)
            self.start_episode()
        Movements.kinect_state = current_state

    def start_episode(self):
        print("start episode")
        Movements.is_running += 1
        #time.sleep(1)
        self.run()

    def run(self):
        # set to initial position
        self.run_traj(self.base_traj)
        k = 0
        t0 = time.time()
        dt = time.time() - t0
        print('run', Movements.is_running, k)
        while dt < self.episode_length and Movements.is_running == 1:
            # generate a random motion
            num = random.randint(1, len(self.traj)) - 1
            self.run_traj(self.traj[num])
            self.run_traj(self.base_pos)
            dt = time.time() - t0
            print(int(dt), k)
            k+=1
        Movements.is_running -= 1
        print("exit", Movements.is_running)


    def run_traj(self, t):
        # t - trajectory
        for m in t:
            if Movements.is_running == 1:
                if 'pos' in m:
                    self.publish(m['pos'])
                if 'delay' in m:
                    time.sleep(m['delay'])

    def init_traj(self):
        # movement 1
        move = []
        move.append({'pos': '-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1', 'delay': 1})
        move.append({'pos': '-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1', 'delay': 1})
        move.append({'pos': '-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1', 'delay': 1})
        self.traj.append(move)

        # movement 1
        move = []
        move.append({'pos': '-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1', 'delay': 1})
        move.append({'pos': '-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1', 'delay': 1})
        move.append({'pos': '-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1', 'delay': 1})
        self.traj.append(move)



if __name__ == '__main__':
    try:
        m = Movements()
        m.start_episode()

    except rospy.ROSInterruptException:
        pass