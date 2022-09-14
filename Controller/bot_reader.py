import config
import telebot
from Model import logic

bot = telebot.TeleBot(config.key)


def why_me(message):
    print(f'Проверка пользователя{message.chat.id}')
    user = logic.get_user(message.chat.id)
    if not user:
        print(f'Ошибка авторизации пользователя {message.chat.id}')
    return user


@bot.message_handler(commands=["start"])
def start(message):
    user = why_me(message)
    if not user:
        logic.registration(message)
    else:
        logic.welcome(user)


'''
@bot.message_handler(commands=["start"])
def start(message):
    logic.create_user(message.chat.id)
    user = why_me(message)
'''


@bot.message_handler(commands=["admin"])
def admin(message):
    user = why_me(message)
    logic.admin_command(user, message.text)


@bot.message_handler(commands=["info_user"])
def info_user(message):
    user = why_me(message)
    logic.user_info_db(user.chat_id)


@bot.message_handler(content_types=['text'])
def request(message):
    user = why_me(message)
    options = logic.get_active_keyboard(user)
    text = message.text
    if logic.main_options in options:
        logic.main_key(user, text)
    if logic.necromancy_options in options:
        pass
    if logic.skel_work_options in options:
        pass
    if logic.work_options in options:
        pass
    if 'manual' in options:
        logic.manual_callback(user, text)
    if 'skel_create' in options:
        logic.skel_create_callback(user, text)
    if 'skel_work' in options:
        logic.skel_work_callback(user, text)
    else:
        logic.undefait_text(user)


def start_event(user):
    text, keyboard = logic.why_event(user)
    bot.send_message(user.chat_id, text, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    user = why_me(call.message)
    if call.data == 'confirm':
        bot.send_message(user.chat_id, 'confirm')
    if call.data == 'start_attack':
        text = logic.event_attack(user)
        bot.send_message(user.chat_id, text)
    if call.data == 'cancel_attack':
        bot.send_message(user.chat_id, 'cancel_attack')


def bot_send(user, text):
    bot.send_message(user.chat_id, text)


bot.polling(none_stop=True, interval=0)
