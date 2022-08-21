import Necromant_class
import balance

user_list = {}


def create_user(chat_id='test'):
    new_user = Necromant_class.Necromant(chat_id)
    user_list.update({chat_id: new_user})
    return new_user


def get_user(chat_id):
    users = user_list.keys()
    if chat_id in users:
        return True, user_list[chat_id]
    else:
        return False, create_user()



def kill_human(me):
    me.take_energy()
    me.add_bones(balance.bones_for_kill_human)


def go_work(me):
    me.take_energy()
    me.add_gold(balance.gold_for_work)


def create_skeleton(me):
    me.take_energy(1)
    me.take_bones(balance.skeleton_for_bones)
    me.set_skeletons('waiter', 1)


def skeleton_go_to(me, work, count=1):
    """Ввести из farmer defer attacker"""
    if work not in me.skeletons:
        print('Error skeleton_go_to type')
    me.set_skeletons('waiter', -1)
    me.set_skeletons(work, count)


def take_from_farm_bone(me, dif_time=1):
    farm_bone(me, dif_time)


def farm_bone(me, iteration=1):
    me.bones += me.skeletons.get('farmer') * 5 * iteration


def attack(me, skeletons_death=0, change_read_book=0):
    me.bones += me.skeletons.get('attacker') * 5
    me.set_skeletons('attacker', skeletons_death * -1)
    if change_read_book == 1:
        me.lvlup()


def event_def(me, rouges=1):
    def_skels = me.skeletons.get('defer')
    lost = fight(rouges, def_skels)
    after_fight = rouges - lost[0] * 10 + def_skels - lost[1] * 5
    me.set_skeletons('defer', def_skels - lost[1] * -1)
    win_skels = lost[2]
    if win_skels:
        me.add_bones(after_fight)
    else:
        me.take_gold(lost[0] * 10)


def fight(units, skels):
    if skels >= units:
        bg = [0, skels - units, 1]
    else:
        bg = [units - skels, 0, 0]
    return bg


def wait(me, count=1):
    me.add_enegry(count)


def user_info(me):
    return f'{me.chat_id}:\nenergy = {me.energy}, \nbones = {me.bones}, \ngold = {me.gold}, \nlevel = {me.level}, \nskeletons = {me.skeletons}\n'
