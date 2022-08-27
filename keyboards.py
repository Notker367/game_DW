import telebot as bot

import Texts

k_button = bot.types.KeyboardButton
text_b = Texts.Text_for.button


def keyboard_create(buttons):
    keyboard = bot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    if 'info' in buttons:
        keyboard = add_info(keyboard)
    if 'manual' in buttons:
        keyboard = add_manual(keyboard)
    if 'skel_create' in buttons:
        keyboard = add_skeleton_create(keyboard)
    if 'skel_work' in buttons:
        keyboard = add_skeleton_work(keyboard)
    return keyboard


def add_info(keyboard):
    info_but = k_button('/info')
    keyboard.add(info_but)
    return keyboard


def add_manual(keyboard):
    kill_hum_but = k_button(text_b['kill_hum'])
    work_but = k_button(text_b['work'])
    keyboard.add(kill_hum_but, work_but)
    return keyboard


def add_skeleton_create(keyboard):
    create_skeleton_but = k_button(text_b['bones_to_skeleton'])
    keyboard.add(create_skeleton_but)
    return keyboard


def add_skeleton_work(keyboard):
    to_farmer_but = k_button(text_b['to_farmer'])
    to_defer_but = k_button(text_b['to_defer'])
    to_attacker_but = k_button(text_b['to_attacker'])
    keyboard.add(to_farmer_but, to_defer_but, to_attacker_but)
    return keyboard
