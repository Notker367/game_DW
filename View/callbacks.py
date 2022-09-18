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
    return f'Привет {user.name}'


def info_necr(necr: roles.Necromant):
    return f'Запас дней: {necr.energy}\n ' \
           f'Золото: {necr.gold}/{necr.get_max_gold()}\n' \
           f'Кости: {necr.bones}/{necr.get_max_bones()}\n' \
           f'Прочитанные страницы: {necr.level}/{balance.max_level_start}'


def necromancy_text(necr: roles.Necromant):
    necromancy_info = f'Ур. Некромантии: {necr.level}\n' \
                      f'Костей: {necr.bones}/{necr.get_max_bones()}\n' \
                      f'Всего скелетов: {necr.get_all_skeletons()}/{necr.get_maximum_skeletons()}\n' \
                      f'Свободных: {necr.skeletons.get("waiter")}\n' \
                      f'Собиратель: {necr.skeletons.get("farmer")}\n' \
                      f'Защитник: {necr.skeletons.get("defer")}\n' \
                      f'Атакующий:  {necr.skeletons.get("attacker")}'
    return necromancy_info


def registration(user):
    return f'{user.username}, вы зарегистрированы'


def skills(necr: roles.Necromant):
    text_for_necr_lvl = Texts.Text_for.skills[f'lvl{str(necr.level)}']
    return text_for_necr_lvl


def skeletons_management(necr):
    text_skel_info = f'Всего скилеотов: {necr}'
    pass
