import random

# bones
bones_for_kill_human = 20
bones_for_kill_skeleton = 5
bones_for_kill_rouge = 10

# gold
gold_for_work = 20
gold_for_rouge = 10

# skeleton
skeleton_need_bones = 20
need_attackers_for_attack = 1

# energy
max_energy = 20
time_for_add_energy = 5  # sec

# events
event_cd = 5  # sec

event_def_roll = 10  # %
event_attack_roll = 30  # %

# fight
win_skels_change_def = 60  # %

# level
change_read_book = 20  # %


def roll(start=0, end=100):
    return random.randrange(start, end)
