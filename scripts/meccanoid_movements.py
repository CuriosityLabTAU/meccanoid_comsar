class MeccanoidMovements():
    all_traj = {}
    meccanoid_morphology = 'humanoid'
    the_traj = []

    def __init__(self, morphology="humanoid"):
        self.set_humanoid()
        self.set_dinosaur()

        self.meccanoid_morphology = morphology
        print("======= " , self.meccanoid_morphology, "============")

        self.the_traj = self.all_traj[self.meccanoid_morphology]

    def set_humanoid(self):
        self.all_traj['humanoid'] = {}
        t = self.all_traj['humanoid']
        t['base_pos'] = [{'pos': '122,238,23,27,132,14,231,227,0,0,0,0,0,0,0,0', 'delay': 1}]
        t['base_traj'] = [{'pos': '122,238,23,27,132,14,231,227,0,0,0,0,0,0,0,0', 'delay': 1}]

        # movement headtilt
        move = []
        move.append({'pos': '84,236,23,20,128,11,231,227,0,0,0,0,0,0,0,0', 'delay': 1})
        t['head tilt'] = move

        # movement headleftright
        move = []
        move.append({'pos': '116,236,23,20,205,11,231,227,0,0,0,0,0,0,0,0', 'delay': 0.05})
        move.append({'pos': '122,236,23,20,52,11,231,227,0,0,0,0,0,0,0,0', 'delay': 0.05})
        move.append({'pos': '116,236,23,20,205,11,231,227,0,0,0,0,0,0,0,0', 'delay': 0.05})
        t['headleftright'] = move

        # movement left shoulder
        move = []
        move.append({'pos': '122,123,23,19,124,11,231,227,0,0,0,0,0,0,0,0', 'delay': 0.05})
        t['leftshoulder'] = move

        # movement right shoulder
        move = []
        move.append({'pos': '122,228,23,20,124,136,229,237,0,0,0,0,0,0,0,0', 'delay': 0.05})
        t['rightshoulder'] = move

        # movement left hand wave
        move = []
        move.append({'pos': '122,133,127,6,124,12,230,234,0,0,0,0,0,0,0,0', 'delay': 0.05})
        move.append({'pos': '122,133,127,82,124,12,230,234,0,0,0,0,0,0,0,0', 'delay': 0.05})
        move.append({'pos': '122,133,127,6,124,12,230,234,0,0,0,0,0,0,0,0', 'delay': 0.05})
        move.append({'pos': '122,133,127,82,124,12,230,234,0,0,0,0,0,0,0,0,', 'delay': 0.05})
        move.append({'pos': '122,133,127,6,124,12,230,234,0,0,0,0,0,0,0,0', 'delay': 0.05})
        t['lefthandwave'] = move

        # movement right hand wave
        move = []
        move.append({'pos': '122,235,28,17,124,115,117,237,0,0,0,0,0,0,0,0', 'delay': 0.05})
        move.append({'pos': '122,234,28,16,124,116,117,179,0,0,0,0,0,0,0,0', 'delay': 0.05})
        move.append({'pos': '122,235,28,17,124,115,117,237,0,0,0,0,0,0,0,0', 'delay': 0.05})
        move.append({'pos': '122,234,28,16,124,116,117,179,0,0,0,0,0,0,0,0', 'delay': 0.05})
        move.append({'pos': '122,235,28,17,124,115,117,237,0,0,0,0,0,0,0,0', 'delay': 0.05})
        t['righthandwave'] = move

        # movement conductor
        move = []
        move.append({'pos': '122,128,56,55,124,128,180,194,0,0,0,0,0,0,0,0', 'delay': 0.05})
        t['conductor'] = move


    def set_dinosaur(self):
        self.all_traj['dinosaur'] = {}
        t = self.all_traj['dinosaur']
        t['base_pos'] = [
            {'pos': '117,137,132,230,126,231,122,117,0,0,0,0,0,0,0,0', 'delay': 1}]
        t['base_traj'] = [
            {'pos': '117,137,132,230,126,231,122,117,0,0,0,0,0,0,0,0', 'delay': 0.05},
            {'pos': '120,132,138,164,131,234,116,111,0,0,0,0,0,0,0,0', 'delay': 0.05},
            {'pos': '117,137,132,230,126,231,122,117,0,0,0,0,0,0,0,0', 'delay': 0.05}
        ]

        # movement headtilt
        move = []
        move.append({'pos': '117,133,174,230,127,231,122,117,0,0,0,0,0,0,0,0', 'delay': 3})
        t['head tile'] = move

        # movement headleftright
        move = []
        move.append({'pos': '117,198,127,230,127,231,122,117,0,0,0,0,0,0,0,0', 'delay': 1})
        move.append({'pos': '117,81,127,230,127,231,122,117,0,0,0,0,0,0,0,0', 'delay': 1})
        move.append({'pos': '117,198,127,230,127,231,122,117,0,0,0,0,0,0,0,0', 'delay': 1})
        t['headleftright'] = move

        # movement left shoulder
        move = []
        move.append({'pos': '40,136,139,231,127,231,122,117,0,0,0,0,0,0,0,0', 'delay': 3})
        t['leftshoulder'] = move

        # movement right shoulder
        move = []
        move.append({'pos': '120,136,139,231,226,231,122,117,0,0,0,0,0,0,0,0', 'delay': 3})
        t['rightshoulder'] = move

        # movement tail wave left
        move = []
        move.append({'pos': '120,136,140,231,131,86,233,230,0,0,0,0,0,0,0,0', 'delay': 1})
        move.append({'pos': '120,136,140,231,131,96,233,149,0,0,0,0,0,0,0,0', 'delay': 1})
        move.append({'pos': '120,136,140,231,131,86,233,230,0,0,0,0,0,0,0,0', 'delay': 1})
        move.append({'pos': '120,136,140,231,131,96,233,149,0,0,0,0,0,0,0,0', 'delay': 1})
        move.append({'pos': '120,136,140,231,131,86,233,230,0,0,0,0,0,0,0,0', 'delay': 1})
        t['talewaveleft'] = move

        # movement tail wave right
        move = []
        move.append({'pos': '120,136,140,230,131,111,13,222,0,0,0,0,0,0,0,0', 'delay': 1})
        move.append({'pos': '120,136,140,231,131,121,13,159,0,0,0,0,0,0,0,0', 'delay': 1})
        move.append({'pos': '120,136,140,230,131,111,13,222,0,0,0,0,0,0,0,0', 'delay': 1})
        move.append({'pos': '120,136,140,231,131,121,13,159,0,0,0,0,0,0,0,0', 'delay': 1})
        move.append({'pos': '120,136,140,230,131,111,13,222,0,0,0,0,0,0,0,0', 'delay': 1})
        t['talewaveright'] = move

        # movement scorpion
        move = []
        move.append({'pos': '120,136,140,231,131,30,126,230,0,0,0,0,0,0,0,0', 'delay': 3})
        t['scorpion'] = move

        # movement mouth
        move = []
        move.append({'pos': '120,132,138,164,131,234,116,111,0,0,0,0,0,0,0,0', 'delay': 3})
        t['mouth'] = move


"""
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
,       move.append({'pos': '236,23,20,0,11,231,227,0,205,116,0,0,0,0,0,0', 'delay': 1})
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
        move.append({'pos': '133,127,6,0,12,230,234,0,124,122,0,0,0,0,0,0', 'delay': 1}),
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
"""    
