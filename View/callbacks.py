from View import Texts, bot_send, keyboards
from Model import roles, balance

text = Texts.Text_for.callback


def create(user: roles.User):
    pass


'''    
    options = ['main']
    user.set_keyboard(options)
    keyboard = keyboards.keyboard_create(options)
    bot_send.update_keyboard(user, text['create'] + str(user.chat_id), keyboard)
'''


def text_welcome(user: roles.User):
    return f'Привет {user.username}'


def info_necr(necr: roles.Necromant):
    return f'Запас дней: {necr.energy}\n ' \
           f'Золото: {necr.gold}/{necr.get_max_gold()}\n' \
           f'Кости: {necr.bones}/{necr.get_max_bones()}\n' \
           f'Прочитанные страницы: {necr.level}/{balance.max_level_start}'


def necromancy_text(necr: roles.Necromant):
    return f'Ур. Некромантии: {necr.level}'


def registration(user):
    return f'{user.username}, вы зарегистрированы'
