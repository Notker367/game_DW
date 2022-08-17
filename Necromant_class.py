class Necromant:
    energy = 0
    bones = 0
    gold = 0
    level = 0
    skeletons = {'waiter': 0,
                 'farmer': 0,
                 'defer': 0,
                 'attacker': 0,
                 }

    def add_enegry(self, change=1):
        self.energy += change

    def take_energy(self, change=1):
        self.energy -= change

    def add_bones(self, change):
        self.bones += change

    def take_bones(self, change):
        self.bones -= change

    def add_gold(self, change):
        self.bones += change

    def take_gold(self, change):
        self.bones -= change

    def get_skeletons(self, skeleton_type):
        if skeleton_type not in self.skeletons.keys():
            print('Error class Necromant get_skeletons')
        return self.skeletons[skeleton_type]

    def set_skeletons(self, skeleton_type, count):
        if skeleton_type not in self.skeletons.keys():
            print('Error class Necromant set_skeletons')
        self.skeletons[skeleton_type] = self.skeletons[skeleton_type] + count
