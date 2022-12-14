import telebot as bot

from View import Texts

k_button = bot.types.KeyboardButton
text_button = Texts.Text_for.button
text_event = Texts.Text_for.event_button


def keyboard_create(buttons=[]):
    keyboard = bot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    if 'info_user' in buttons:
        keyboard = add_info_user(keyboard)
    if 'start' in buttons:
        keyboard = add_start(keyboard)
    keyboard = mian_options_check(buttons, keyboard)
    keyboard = necromancy_options_check(buttons, keyboard)
    keyboard = work_options_check(buttons, keyboard)
    keyboard = upgrade_options_check(buttons, keyboard)
    if 'back' in buttons:
        keyboard = add_back(keyboard)
    return keyboard


def upgrade_options_check(buttons, keyboard):
    if 'up_basement' in buttons:
        keyboard = add_up_basement(keyboard)
    if 'up_chest' in buttons:
        keyboard = add_up_chest(keyboard)
    if 'up_lvl' in buttons:
        keyboard = add_up_lvl(keyboard)
    return keyboard


def add_up_basement(keyboard):
    up_basement_but = k_button(text_button.get('up_basement'))
    keyboard.add(up_basement_but)
    return keyboard


def add_up_chest(keyboard):
    up_chest_but = k_button(text_button.get('up_chest'))
    keyboard.add(up_chest_but)
    return keyboard


def add_up_lvl(keyboard):
    up_lvl_but = k_button(text_button.get('up_lvl'))
    keyboard.add(up_lvl_but)
    return keyboard


def work_options_check(buttons, keyboard):
    if 'kill_hum' in buttons:
        keyboard = add_kill_hum(keyboard)
    if 'heal_hum' in buttons:
        keyboard = add_heal_hum(keyboard)
    return keyboard


def necromancy_options_check(buttons, keyboard):
    if 'bones_to_skeleton' in buttons:
        keyboard = add_skeleton_create(keyboard)
    if 'to_farmer' in buttons:
        keyboard = add_skeleton_to_farmer(keyboard)
    if 'to_defer' in buttons:
        keyboard = add_skeleton_to_defer(keyboard)
    if 'to_attacker' in buttons:
        keyboard = add_skeleton_to_attacker(keyboard)
    if 'to_reset' in buttons:
        keyboard = add_skeleton_to_reset(keyboard)
    return keyboard


def mian_options_check(buttons, keyboard):
    if 'info_necr' in buttons:
        keyboard = add_info_necr(keyboard)
    if 'work' in buttons:
        keyboard = add_work(keyboard)
    if 'necromancy' in buttons:
        keyboard = add_necromancy(keyboard)
    if 'upgrade' in buttons:
        keyboard = add_upgrade(keyboard)
    return keyboard


def add_start(keyboard):
    start_but = k_button('/start')
    keyboard.add(start_but)
    return keyboard


def add_info_user(keyboard):
    info_but = k_button('/info_user')
    keyboard.add(info_but)
    return keyboard


def add_upgrade(keyboard):
    upgrade_but_text = text_button.get('upgrade')
    keyboard.keyboard[2].append({'text': upgrade_but_text})
    return keyboard


def add_back(keyboard):
    back_but = k_button(text_button.get('back'))
    keyboard.add(back_but)
    return keyboard


def add_skills(keyboard):
    skill_but = k_button(text_button.get('skills'))
    keyboard.add(skill_but)
    return keyboard


def add_kill_hum(keyboard):
    kill_hum_but = k_button(text_button['kill_hum'])
    keyboard.add(kill_hum_but)
    return keyboard


def add_heal_hum(keyboard):
    heal_hum_but = k_button(text_button['heal_hum'])
    keyboard.add(heal_hum_but)
    return keyboard


def add_skeleton_create(keyboard):
    create_skeleton_but = k_button(text_button['bones_to_skeleton'])
    keyboard.add(create_skeleton_but)
    return keyboard


def add_skeleton_work(keyboard):
    skel_work_but = k_button(text_button['skel_work'])
    keyboard.add(skel_work_but)
    return keyboard


def add_skeleton_to_farmer(keyboard):
    to_farmer_text = text_button['to_farmer']
    to_farmer_but = k_button(to_farmer_text)

    if len(keyboard.keyboard) >= 2:
        keyboard.keyboard[1].append(to_farmer_text)
    else:
        keyboard.add(to_farmer_but)
    return keyboard


def add_skeleton_to_defer(keyboard):
    to_defer_text = text_button['to_defer']
    to_defer_but = k_button(to_defer_text)

    if len(keyboard.keyboard) >= 2:
        keyboard.keyboard[1].append(to_defer_text)
    else:
        keyboard.add(to_defer_but)
    return keyboard


def add_skeleton_to_attacker(keyboard):
    to_attacker_text = text_button['to_attacker']
    to_attacker_but = k_button(to_attacker_text)

    if len(keyboard.keyboard) >= 2:
        keyboard.keyboard[1].append(to_attacker_text)
    else:
        keyboard.add(to_attacker_but)
    return keyboard


def add_skeleton_to_reset(keyboard):
    to_reset_but = k_button(text_button['to_reset'])
    keyboard.add(to_reset_but)
    return keyboard


def keyboard_inline_create(buttons=[]):
    """
    ????????????????

    :param: buttons: confirm,attack

    :return: sad
    """
    keyboard = bot.types.InlineKeyboardMarkup()
    if 'confirm' in buttons:
        keyboard = event_confirm(keyboard)
    if 'attack' in buttons:
        keyboard = event_attack(keyboard)
    return keyboard


def event_confirm(keyboard):
    """
    ?????????????????? ?????????? ???????????? ??????????????

    :param keyboard:
    :return: keyboard
    """
    confirm_but = bot.types.InlineKeyboardButton(text=text_event['confirm'], callback_data='confirm')
    keyboard.add(confirm_but)
    return keyboard


def event_attack(keyboard):
    """
    ?????????????????? ?????????? ???????????? ???????????? ?????????? ?? ???????????????? ??????????

    :param keyboard:
    :return: keyboard
    """
    start_attack_but = bot.types.InlineKeyboardButton(text=text_event['start_attack'], callback_data='start_attack')
    cancel_attack_but = bot.types.InlineKeyboardButton(text=text_event['cancel_attack'], callback_data='cancel_attack')
    keyboard.add(start_attack_but, cancel_attack_but)
    return keyboard


def main():
    keyboard = keyboard_create()
    info_necr_but = k_button(text_button['necr_info'])
    work_but = k_button(text_button['work'])
    necromancy_but = k_button(text_button['necromancy'])
    keyboard.add(info_necr_but, work_but, necromancy_but, row_width=1)
    return keyboard


def add_info_necr(keyboard):
    info_necr_but = k_button(text_button['necr_info'])
    keyboard.add(info_necr_but)
    return keyboard


def add_work(keyboard):
    work_but = k_button(text_button['work'])
    keyboard.add(work_but)
    return keyboard


def add_necromancy(keyboard):
    necromancy_but = k_button(text_button['necromancy'])
    keyboard.add(necromancy_but)
    return keyboard
