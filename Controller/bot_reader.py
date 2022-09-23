import config
import telebot
from Model import logic

bot = telebot.TeleBot(config.key)


def why_me(message):
    print(f'Проверка пользователя {message.chat.id}')
    user = logic.get_user(message.chat.id)
    if not user:
        print(f'Ошибка авторизации пользователя {message.chat.id}')
        return False
    return user


@bot.message_handler(commands=["kill_me"])
def kill_me(message):
    print(fast.end.program)


@bot.message_handler(commands=["start"])
def start(message):
    user = why_me(message)
    if not user:
        logic.registration(message)
    else:
        logic.welcome(user)


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
    if not user:
        logic.undefait_text_no_user(message)
    options = logic.get_active_keyboard(user)
    text = message.text

    if logic.back_key(user, text):
        logic.main_keyboard(user)

    elif set(options).issubset(logic.main_options):
        logic.main_key(user, text)

    elif set(options).issubset(logic.work_options):
        logic.work_key(user, text)

    elif set(options).issubset(logic.necromancy_options):
        logic.necromancy_key(user, text)

    elif set(options).issubset(logic.upgrade_options):
        logic.upgrade_key(user, text)

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
