import telebot
import Texts

bot = telebot.TeleBot('5674536023:AAHriUyut4AuXLfPV9HP_xeiPxVGHkPoegc')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, Texts.Text_for.welcome)


bot.polling()
