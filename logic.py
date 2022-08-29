import Necromant_class
import balance
import keyboards
from Texts import Text_for

user_list = {}
request_text = {}
users_time = {}
need_event = False


def create_user(chat_id='test'):
    new_user = Necromant_class.Necromant(chat_id)
    user_list.update({chat_id: new_user})
    return new_user


def get_active_keyboard(me: Necromant_class):
    return me.get_keyboard()


def set_active_keyboard(me: Necromant_class, buttons):
    me.set_keyboard(buttons)


def get_user(chat_id):
    users = user_list.keys()
    if chat_id in users:
        return True, user_list[chat_id]
    else:
        return False, create_user(str(chat_id))


def need_send_user(me, texts='need_send_user пустой текст', read=0):
    user_id = me.chat_id
    if read and user_id in request_text.keys():
        return request_text[user_id]
    request_text[user_id] = texts
    return texts


def kill_human(me):
    me.take_energy()
    me.add_bones(balance.bones_for_kill_human)


def go_work(me):
    me.take_energy()
    me.add_gold(balance.gold_for_work)


def create_skeleton(me):
    # me.take_energy(1)
    me.take_bones(balance.skeleton_need_bones)
    me.set_skeletons('waiter', 1)


def skeleton_go_to(me, work, count=1):
    """Ввести из farmer defer attacker"""
    if work not in me.skeletons:
        print('Error skeleton_go_to type')
    me.set_skeletons('waiter', count * -1)
    me.set_skeletons(work, count)


def take_from_farm_bone(me, dif_time=1):
    farm_bone(me, dif_time)


def farm_bone(me, iteration=1):
    me.bones += me.skeletons.get('farmer') * 5 * iteration


def event_attack(me):
    guards = 1
    skeletons = me.skeletons.get('attacker')
    lost = fight(guards, skeletons, balance.win_skels_change_attack)
    guards_lost, skeletons_lost = lost[0], lost[1]
    skeletons_death = skeletons - skeletons_lost
    after_fight = guards - guards_lost * balance.bones_for_kill_guard \
                  + skeletons_death * balance.bones_for_kill_skeleton
    skeletons_win = lost[0] == 0
    if skeletons_win:
        me.add_bones(after_fight)
        if balance.roll() <= balance.change_read_book:
            me.lvlup()
    me.set_skeletons('attacker', skeletons_death * -1)
    return Text_for.event_text['skeletons_win'] if skeletons_win \
        else Text_for.event_text['skeletons_lose']


def event_def(me, rouges=1):
    def_skels = me.skeletons.get('defer')
    lost = fight(rouges, def_skels, balance.win_skels_change_def)
    after_fight = rouges - lost[0] * balance.bones_for_kill_rouge \
                  + def_skels - lost[1] * balance.bones_for_kill_skeleton
    me.set_skeletons('defer', (def_skels - lost[1]) * -1)
    skeletons_win = lost[0] == 0
    if skeletons_win:
        me.add_bones(after_fight)
    else:
        me.take_gold(lost[0] * balance.gold_for_rouge)


def fight(units, skels, win_skels_change):
    """
    Битва пока кого-то не станет 0

    :param units: Кол-во противников
    :param skels: Кол-во скелетов
    :param win_skels_change: Шанс что выграет скилет 1 на 1 с units в %
    :return: list[units, skels]
    """
    bg = [units, skels]
    while not (0 in bg):
        if balance.roll() <= win_skels_change:
            bg[0] -= 1
        else:
            bg[1] -= 1
    return bg


def time_step(me, time):
    try:
        prew_time = users_time[me.chat_id]
    except:
        users_time[me.chat_id] = time
        return
    d_time = time - prew_time
    step_energy(me, d_time)
    check_event(me, d_time)
    users_time[me.chat_id] = time


def check_event(me, time):
    global need_event
    if me.cd_event <= 0:
        me.cd_event = balance.event_cd
        need_event = True
    else:
        me.cd_event = me.cd_event - time
        need_event = False


def step_energy(me, time):
    need_add_energy = time // balance.time_for_add_energy
    energy_after = me.energy + need_add_energy
    if energy_after > balance.max_energy:
        me.energy = balance.max_energy
    elif energy_after <= balance.max_energy:
        me.add_energy(need_add_energy)
    else:
        print('Error logic step_energy')


def energy_add(me, count=1):
    me.add_energy(count)


def user_info(me):
    return f'{me.chat_id}:\nenergy = {me.energy}, ' \
           f'\nbones = {me.bones}, ' \
           f'\ngold = {me.gold}, ' \
           f'\nlevel = {me.level}, ' \
           f'\ntest = {me.cd_event}\n' \
           f'\nskeletons = {me.skeletons}\n'


def energy_check(me, need_energy=1):
    if me.energy >= need_energy:
        have_energy = True
    else:
        have_energy = False
    return have_energy


def skeleton_waiter_check(me, need_waiter=1):
    if me.skeletons['waiter'] >= need_waiter:
        return True
    else:
        return False


def bones_check(me, need_bones):
    if me.bones >= need_bones:
        return True
    else:
        return False


def text_reader(me, text):
    # print('Error text_reader')
    params = me.get_keyboard()
    # ['info', 'manual', 'skel_create', 'skel_work']
    if text not in Text_for.button.values():
        need_send_user(me, Text_for.Error['no_commands'])
    if 'manual' in params:
        manual_collback(me, text)
    if 'skel_create' in params:
        skel_create_collback(me, text)
    if 'skel_work' in params:
        skel_work_collback(me, text)
    return
    # need_send_user(me, request_text)


def manual_collback(me, text):
    need_kill_hum = text == Text_for.button['kill_hum']
    need_work = text == Text_for.button['work']
    energy = energy_check(me)
    if need_kill_hum and energy:
        kill_human(me)
        need_send_user(me, Text_for.complite['kill_hum'])
    elif need_work and energy:
        go_work(me)
        need_send_user(me, Text_for.complite['work'])
    elif (need_work or need_kill_hum) and not energy:
        need_send_user(me, Text_for.Error['no_energy'])


def skel_create_collback(me, text):
    need_skel_create = text == Text_for.button['bones_to_skeleton']
    have_bones = bones_check(me, balance.skeleton_need_bones)
    if need_skel_create and have_bones:
        create_skeleton(me)
        need_send_user(me, Text_for.complite['bones_to_skeleton'])
    elif need_skel_create and not have_bones:
        need_send_user(me, Text_for.Error['no_bones'])


def skel_work_collback(me, text):
    need_farmer = text == Text_for.button['to_farmer']
    need_defer = text == Text_for.button['to_defer']
    need_attacker = text == Text_for.button['to_attacker']
    have_waiter = skeleton_waiter_check(me)
    if need_farmer and have_waiter:
        skeleton_go_to(me, 'farmer')
        need_send_user(me, Text_for.complite['to_farmer'])
    elif need_defer and have_waiter:
        skeleton_go_to(me, 'defer')
        need_send_user(me, Text_for.complite['to_defer'])
    elif need_attacker and have_waiter:
        skeleton_go_to(me, 'attacker')
        need_send_user(me, Text_for.complite['to_attacker'])
    elif (need_farmer or need_defer or need_attacker) and not have_waiter:
        need_send_user(me, Text_for.Error['no_waiter'])


def why_event(me):
    roll_event = balance.roll()
    attackers = me.skeletons['attacker']
    if roll_event <= balance.event_def_roll \
            and me.gold >= balance.gold_for_def_event:  # def_event
        rouges = balance.roll(0, (me.gold // balance.gold_for_rouge))
        event_def(me, rouges)
        return Text_for.event_text['def'], keyboards.keyboard_inline_create(['confirm'])
    elif roll_event <= balance.event_attack_roll \
            and attackers >= balance.need_attackers_for_attack_event:  # attack event
        return Text_for.event_text['attack'], keyboards.keyboard_inline_create(['attack'])
    else:
        return Text_for.event_text['none'], None
