import Necromant_class
import balance
from Necromant_class import Necromant

me: Necromant = Necromant_class.Necromant()


def kill_human():
    me.take_energy()
    me.add_bones(balance.bones_for_kill_human)


def go_work():
    me.take_energy()
    me.add_gold(balance.gold_for_work)


def create_skeleton():
    me.take_energy(1)
    me.take_bones(balance.skeleton_for_bones)
    me.set_skeletons('waiter', 1)


def skeleton_go_to(work, count=1):
    """Ввести из farmer defer attacker"""
    if work not in me.skeletons:
        print('Error skeleton_go_to type')
    me.set_skeletons('waiter', -1)
    me.set_skeletons(work, count)


def take_from_farm_bone(dif_time=1):
    farm_bone(dif_time)


def farm_bone(iteration=1):
    me.bones += me.skeletons.get('farmer') * 5 * iteration


def attack(skeletons_death=0, change_read_book=0):
    me.bones += me.skeletons.get('attacker') * 5
    me.set_skeletons('attacker', skeletons_death * -1)
    if change_read_book == 1:
        me.lvlup()


def wait(count=1):
    me.add_enegry(count)


def me_info():
    print(
        f'energy = {me.energy}, \nbones = {me.bones}, \ngold = {me.gold}, \nlevel = {me.level}, \nskeletons = {me.skeletons}\n')
