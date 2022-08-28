import config
import telebot
import logic
import admin_commands
import keyboards
import Texts

bot = telebot.TeleBot(config.key)


def why_me(message):
    user = logic.get_user(message.chat.id)
    if not user[0]:
        bot.send_message(message.chat.id, 'Error user')
    return user[1]


@bot.message_handler(commands=["start"])
def start(message):
    logic.create_user(message.chat.id)
    user = why_me(message)
    logic.set_active_keyboard(user, ['info', 'manual', 'skel_create', 'skel_work'])
    keyboard = keyboards.keyboard_create(logic.get_active_keyboard(user))
    bot.send_message(message.chat.id, f"Создан некр {user.chat_id}", reply_markup=keyboard)


@bot.message_handler(commands=["admin"])
def admin(message):
    text = message.text
    if text == '/admin':
        bot.send_message(message.chat.id, Texts.Text_for.admin)
    else:
        user = why_me(message)
        admin_commands.cheats(user, text)
        bot.send_message(message.chat.id, 'OK')


@bot.message_handler(commands=["info"])
def info(message):
    user = why_me(message)
    bot.send_message(message.chat.id, logic.user_info(user))


@bot.message_handler(content_types=['text'])
def request(message):
    user = why_me(message)
    logic.text_reader(user, message.text)
    logic.time_step(user, message.date)
    bot.send_message(user.chat_id, logic.need_send_user(user, read=1))


def bot_send(user, text):
    bot.send_message(user.chat_id, text)


bot.polling()
