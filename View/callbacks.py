from View import Texts, bot_send, keyboards

text = Texts.Text_for.callback


def create(user):
    keyboard = keyboards.keyboard_create(['info', 'manual', 'skel_create', 'skel_work'])
    bot_send.update_keyboard(user, text['create'] + str(user.chat_id), keyboard)


