from View import Texts, bot_send, keyboards

text = Texts.Text_for.callback


def create(user):
    options = ['info', 'manual', 'skel_create', 'skel_work']
    user.set_keyboard(options)
    keyboard = keyboards.keyboard_create(options)
    bot_send.update_keyboard(user, text['create'] + str(user.chat_id), keyboard)


def text_created(user):
    return f'Привет {user.name}'
