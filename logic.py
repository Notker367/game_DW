import Necromant_class
import balance

me = Necromant_class.Necromant()


def kill_human():
    me.take_energy()
    me.add_bones(balance.bones_for_kill_human)


def go_work():
    me.take_energy()
    me.add_gold(balance.gold_for_work)


def create_skeleton():
    me.take_energy(0)
    me.take_bones(balance.skeleton_for_bones)
    me.set_skeletons('waiter', 1)


def wait():
    me.add_enegry()


def me_info():
    print(
        f'energy = {me.energy}, \nbones = {me.bones}, \ngold = {me.gold}, \nlevel = {me.level}, \nskeletons = {me.skeletons}')
