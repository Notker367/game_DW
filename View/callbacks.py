from View import Texts, bot_send, keyboards

text = Texts.Text_for.callback


def create(user):
    options = ['main']
    user.set_keyboard(options)
    keyboard = keyboards.keyboard_create(options)
    bot_send.update_keyboard(user, text['create'] + str(user.chat_id), keyboard)


def text_welcome(user):
    return f'Привет {user.username}'


def info_necr(necr):
    return f'Запас дней: {necr.energy}\n' \
           f'Золото: {necr.gold}\n' \
           f'Кости: {necr.bones}\n' \
           f'Прочитанные страницы: {necr.level}'
