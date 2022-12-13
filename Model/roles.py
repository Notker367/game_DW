from Model import balance


class Necromant:

    def __init__(self, energy=2, bones=0, gold=0, level=0,
                 keyboard=None, skeletons=None,
                 cd_event=0, lvl_basement=0, lvl_chest=0):
        self.energy = energy
        self.bones = bones
        self.gold = gold
        self.level = level
        self.keyboard = keyboard
        if keyboard is None:
            self.keyboard = []
        self.skeletons = skeletons
        if skeletons is None:
            self.skeletons = {'waiter': 0,
                              'farmer': 0,
                              'defer': 0,
                              'attacker': 0}
        self.cd_event = cd_event
        self.lvl_basement = lvl_basement
        self.lvl_chest = lvl_chest

    def to_dict(self):
        necromant = {
            'energy': self.energy,
            'bones': self.bones,
            'gold': self.gold,
            'level': self.level,
            'keyboard': self.keyboard,
            'skeletons': self.skeletons,
            'cd_event': self.cd_event,
            'lvl_basement': self.lvl_basement,
            'lvl_chest': self.lvl_chest
        }
        return necromant

    @staticmethod
    def from_dict(necr_info: dict):
        necromant = Necromant(
            energy=necr_info.get('energy'),
            bones=necr_info.get('bones'),
            gold=necr_info.get('gold'),
            level=necr_info.get('level'),
            keyboard=necr_info.get('keyboard'),
            skeletons=necr_info.get('skeletons'),
            cd_event=necr_info.get('cd_event'),
            lvl_basement=necr_info.get('lvl_basement'),
            lvl_chest=necr_info.get('lvl_chest')
        )
        return necromant

    def get_all_skeletons(self):
        all_skeletons = self.skeletons.get('waiter') + \
                        self.skeletons.get('farmer') + \
                        self.skeletons.get('defer') + \
                        self.skeletons.get('attacker')
        return all_skeletons

    def get_maximum_skeletons(self):
        max_skel = self.level * balance.max_skeletons_for_lvl
        return max_skel

    def add_energy(self, change=1):
        self.energy += change

    def take_energy(self, change=1):
        self.energy -= change

    def add_bones(self, change):
        self.bones += change

    def take_bones(self, change):
        self.bones -= change

    def add_gold(self, change):
        self.gold += change

    def take_gold(self, change):
        self.gold -= change

    def get_skeletons(self, skeleton_type):
        if skeleton_type not in self.skeletons.keys():
            print('Error class Necromant get_skeletons')
        return self.skeletons[skeleton_type]

    def set_skeletons(self, skeleton_type, count):
        if skeleton_type not in self.skeletons.keys():
            print('Error class Necromant set_skeletons')
        self.skeletons[skeleton_type] = self.skeletons[skeleton_type] + count

    def lvlup(self):
        self.level += 1

    def set_lvl(self, lvl):
        self.level = lvl

    def get_keyboard(self):
        if self.keyboard == [] or None:
            return False
        return self.keyboard

    def up_lvl_chest(self):
        self.lvl_chest += 1

    def up_lvl_basement(self):
        self.lvl_basement += 1

    def set_keyboard(self, buttons: list):
        self.keyboard = buttons

    def get_max_gold(self):
        max_gold = balance.max_gold_start + self.lvl_chest * balance.max_gold_for_lvl_chest
        return max_gold

    def get_max_bones(self):
        max_bones = balance.max_bones_start + self.lvl_basement * balance.max_gold_for_lvl_chest
        return max_bones

    def info(self):
        return f'PIVO :\nenergy = {self.energy}, ' \
               f'\nbones = {self.bones}, ' \
               f'\ngold = {self.gold}, ' \
               f'\nlevel = {self.level}, ' \
               f'\ntest = {self.cd_event}\n' \
               f'\nskeletons = {self.skeletons}\n'


class Story:
    def __init__(self, part='story0', choice=[]):
        self.part = part
        self.choice = choice

    def to_dict(self):
        story = {
            'part': self.part,
            'choice': self.choice
        }
        return story

    @staticmethod
    def from_dict(story_info: dict):
        story = Story(
            part=story_info.get('part'),
            choice=story_info.get('choice')
        )
        return story


class User:

    def __init__(self, chat_id, necromant: Necromant = None, name='null', username='null', create_time=0):
        self.chat_id = chat_id
        self.necromant = necromant
        self.name = name
        self.username = username
        self.create_time = create_time

    @staticmethod
    def from_dict(user_info):
        user = User(chat_id=user_info.get('chat_id'),
                    name=user_info.get('name'),
                    username=user_info.get('username'),
                    create_time=user_info.get('create_time')
                    )
        return user

    def to_dict(self):
        user = {
            'chat_id': self.chat_id,
            'name': self.name,
            'username': self.username,
            'create_time': self.create_time,
        }
        return user
