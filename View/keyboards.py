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
    return keyboard


def work_options_check(buttons, keyboard):
    if 'kill_hum' in buttons:
        keyboard = add_kill_hum(keyboard)
    if 'heal_hum' in buttons:
        keyboard = add_heal_hum(keyboard)
    return keyboard


def necromancy_options_check(buttons, keyboard):
    if 'skills' in buttons:
        keyboard = add_skills(keyboard)
    if 'skel_create' in buttons:
        keyboard = add_skeleton_create(keyboard)
    if 'skel_work' in buttons:
        keyboard = add_skeleton_work(keyboard)
    return keyboard


def mian_options_check(buttons, keyboard):
    if 'info_necr' in buttons:
        keyboard = add_info_necr(keyboard)
    if 'work' in buttons:
        keyboard = add_work(keyboard)
    if 'necromancy' in buttons:
        keyboard = add_necromancy(keyboard)
    return keyboard


def add_start(keyboard):
    start_but = k_button('/start')
    keyboard.add(start_but)
    return keyboard


def add_info_user(keyboard):
    info_but = k_button('/info_user')
    keyboard.add(info_but)
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
    to_farmer_but = k_button(text_button['to_farmer'])
    keyboard.add(to_farmer_but)
    return keyboard


def add_skeleton_to_defer(keyboard):
    to_defer_but = k_button(text_button['to_defer'])
    keyboard.add(to_defer_but)
    return keyboard


def add_skeleton_to_attacker(keyboard):
    to_attacker_but = k_button(text_button['to_attacker'])
    keyboard.add(to_attacker_but)
    return keyboard


def add_skeleton_to_reset(keyboard):
    to_reset_but = k_button(text_button['to_reset'])
    keyboard.add(to_reset_but)
    return keyboard


def keyboard_inline_create(buttons=[]):
    """
    описание

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
    Добавляет инлай кнопку конфирм

    :param keyboard:
    :return: keyboard
    """
    confirm_but = bot.types.InlineKeyboardButton(text=text_event['confirm'], callback_data='confirm')
    keyboard.add(confirm_but)
    return keyboard


def event_attack(keyboard):
    """
    Добавляет инлай кнопки начать атаку и отменить атаку

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
