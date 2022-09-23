import config
import telebot

# user = user.chat_id
bot = telebot.TeleBot(config.key)


def message(user, text: str):
    bot.send_message(user.chat_id, text)


def update_keyboard(user, text, keyboard):
    bot.send_message(user.chat_id, text, reply_markup=keyboard)


def message_haven_keyboard(user, text, keyboard):
    bot.send_message(user.chat_id, text, reply_markup=keyboard)


def update_keyboard_no_user(message, text, keyboard):
    bot.send_message(message.chat.id, text, reply_markup=keyboard)
