class MeccanoidMovements():
    all_traj = {}
    meccanoid_morphology = 'humanoid'
    the_traj = []
    base_pos = {}
    base_traj = {}
    the_base_pos = []
    the_base_traj = []

    def __init__(self):
        self.set_humanoid()
        self.set_dinosaur()

        self.the_traj = self.all_traj[self.meccanoid_morphology]
        self.the_base_pos = self.base_pos[self.meccanoid_morphology]
        self.the_base_traj = self.base_traj[self.meccanoid_morphology]

    def set_humanoid(self):
        self.base_pos['humanoid'] = [{'pos': '238,23,27,0,14,231,227,0,132,122,0,0,0,0,0,0', 'delay': 1}]
        self.base_traj['humanoid'] = [{'pos': '238,23,27,0,14,231,227,0,132,122,0,0,0,0,0,0', 'delay': 1}]
        self.all_traj['humanoid'] = {}
        t = self.all_traj['humanoid']

        # movement headtilt
        move = []
        move.append({'pos': '236,23,20,0,11,231,227,0,128,84,0,0,0,0,0,0', 'delay': 3})
        t['head tile'] = move

        # movement headleftright
        move = []
        move.append({'pos': '236,23,20,0,11,231,227,0,205,116,0,0,0,0,0,0', 'delay': 1})
        move.append({'pos': '236,23,20,0,11,231,227,0,52,122,0,0,0,0,0,0', 'delay': 1})
        move.append({'pos': '236,23,20,0,11,231,227,0,205,116,0,0,0,0,0,0', 'delay': 1})
        t['headleftright'] = move

        # movement left shoulder
        move = []
        move.append({'pos': '123,23,19,0,11,231,227,0,124,122,0,0,0,0,0,0', 'delay': 3})
        t['leftshoulder'] = move

        # movement right shoulder
        move = []
        move.append({'pos': '228,23,20,0,136,229,237,0,124,122,0,0,0,0,0,0', 'delay': 3})
        t['rightshoulder'] = move

        # movement left hand wave
        move = []
        move.append({'pos': '133,127,6,0,12,230,234,0,124,122,0,0,0,0,0,0', 'delay': 1})
        move.append({'pos': '133,127,82,0,12,230,234,0,124,122,0,0,0,0,0,0', 'delay': 1})
        move.append({'pos': '133,127,6,0,12,230,234,0,124,122,0,0,0,0,0,0', 'delay': 1})
        move.append({'pos': '133,127,82,0,12,230,234,0,124,122,0,0,0,0,0,0,', 'delay': 1})
        move.append({'pos': '133,127,6,0,12,230,234,0,124,122,0,0,0,0,0,0', 'delay': 1})
        t['lefthandwave'] = move

        # movement right hand wave
        move = []
        move.append({'pos': '235,28,17,0,115,117,237,0,124,122,0,0,0,0,0,0', 'delay': 1})
        move.append({'pos': '234,28,16,0,116,117,179,0,124,122,0,0,0,0,0,0', 'delay': 1})
        move.append({'pos': '235,28,17,0,115,117,237,0,124,122,0,0,0,0,0,0', 'delay': 1})
        move.append({'pos': '234,28,16,0,116,117,179,0,124,122,0,0,0,0,0,0,', 'delay': 1})
        move.append({'pos': '235,28,17,0,115,117,237,0,124,122,0,0,0,0,0,0', 'delay': 1})
        t['righthandwave'] = move

        # movement conductor
        move = []
        move.append({'pos': '128,56,55,0,128,180,194,0,124,122,0,0,0,0,0,0', 'delay': 3})
        t['conductor'] = move


    def set_dinosaur(self):
        self.base_pos['dinosaur'] = [
            {'pos': '130,129,229,0,87,156,0,0,230,117,109,0,0,0,0,0', 'delay': 1}]
        self.base_traj['dinosaur'] = [
            {'pos': '90,129,229,0,87,156,0,0,230,117,109,0,0,0,0,0', 'delay': 0.05},
            {'pos': '170,129,229,0,87,156,0,0,230,117,109,0,0,0,0,0', 'delay': 0.05},
            {'pos': '130,129,229,0,87,156,0,0,230,117,109,0,0,0,0,0', 'delay': 0.05}
        ]

        self.all_traj['dinosaur'] = []
        t = self.all_traj['dinosaur']

        '''
        # movement 1
        move = []
        move.append({'pos': '-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1', 'delay': 1})
        move.append({'pos': '-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1', 'delay': 1})
        move.append({'pos': '-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1', 'delay': 1})
        t.append(move)

        # movement 1
        move = []
        move.append({'pos': '-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1', 'delay': 1})
        move.append({'pos': '-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1', 'delay': 1})
        move.append({'pos': '-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1', 'delay': 1})
        t.append(move)
        '''