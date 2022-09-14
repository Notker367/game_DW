import random

# bones
max_bones_start = 50
max_bones_for_lvl_basement = 20
bones_for_kill_human = 5
bones_for_kill_skeleton = 5
bones_for_kill_rouge = 10
bones_for_kill_guard = 20

# gold
max_gold_start = 100
max_gold_for_lvl_chest = 20
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

event_def_roll = 30  # %
event_attack_roll = event_def_roll + 30  # %

# fight
win_skels_change_def = 60  # %
win_skels_change_attack = 40  # %

# level
max_level_start = 5
change_read_book = 20  # %

# time
time_for_clear_stack = 86400  # sec (1d)


def roll(start: int = 0, end: int = 100) -> int:
    if end == 0:
        return 0
    return random.randrange(start, end)
