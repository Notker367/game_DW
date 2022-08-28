import random

# bones
bones_for_kill_human = 20
bones_for_kill_skeleton = 5
bones_for_kill_rouge = 10
bones_for_kill_guard = 20

# gold
gold_for_work = 20
gold_for_rouge = 10
gold_for_def_event = 10

# skeleton
skeleton_need_bones = 20
need_attackers_for_attack_event = 1

# energy
max_energy = 20
time_for_add_energy = 5  # sec

# events
event_cd = 5  # sec

event_def_roll = 10  # %
event_attack_roll = 30  # %

# fight
win_skels_change_def = 60  # %
win_skels_change_attack = 40  # %

# level
change_read_book = 20  # %


def roll(start: int = 0, end: int = 100) -> int:
    if end == 0:
        return 0
    return random.randrange(start, end)
