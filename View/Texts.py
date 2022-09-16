from Model import balance, roles


class Text_for:
    welcome = 'Hi, this welcome text'

    admin = "" \
            "energy <count>\n" \
            "bones <count> \n" \
            "gold <count> \n" \
            "level <count> \n" \
            "skeletons ... \n" \
            "...waiter <count> \n" \
            "...farmer <count>\n " \
            "...defer <count> \n" \
            "...attacker <count>\n"

    button = {'kill_hum': 'Убить пациента',
              'heal_hum': 'Вылечить пациента',
              'work': 'Госпиталь',
              'bones_to_skeleton': 'Создать прислужника',
              'to_farmer': 'Направить скелета собирать кости',
              'to_defer': 'Направить скелета защищать дом',
              'to_attacker': 'Направить скелета в атаку',
              'necr_info': 'info-инвентарь',
              'necromancy': 'Некромантия',
              'skills': 'Навыки',
              'to_reset': 'Вернуть скелетов',
              'skel_work': 'Направить скелетов'}

    Error = {'no_energy': 'Не хватает энергии',
             'no_bones': 'Не хватает костей',
             'no_waiter': 'Нет свободных скелетов',
             'no_commands': 'Нет такой команды',
             'undefait': 'Воспользуйтесь клаивиатурой'}

    complite = {'kill_hum': f'Вы нашли бедалагу которого никто не вспомнит '
                            f'\n +{balance.bones_for_kill_human} костей',
                'heal_hum': f'Получено вознаграждение после тяжелого рабочего дня'
                        f'\n +{balance.gold_for_work} золотых',
                'bones_to_skeleton': f'Еще один прислужник ждет приказа'
                                     f'\n -{balance.skeleton_need_bones} костей',
                'to_farmer': 'Cкелет отправился в лес добыть кости',
                'to_defer': 'Cкелет отправился охранять дом',
                'to_attacker': 'Cкелет отправился готовится к наступлению'}

    event_button = {'confirm': 'Понятненько!',
                    'start_attack': 'Начать атаку',
                    'cancel_attack': 'Отложить атаку'}

    event_text = {'def': 'Атака на дом',
                  'none': 'Ничего не произошло',
                  'attack': 'Отличное время для атаки. Хотите её начать?',
                  'skeletons_win': 'Скелеты победили',
                  'skeletons_lose': 'ti loh'}

    callback = {'create': 'Cоздан пользователь с id '}

    keyboards = {'main': 'вы у себя дома',
                 'work': 'Вы нашли пациента, которого уже не спасти, что с ним делать?',
                 'necromancy': 'PIVO necromancy'}
