import balance


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
    button = {'kill_hum': 'Выкрасть пациента',
              'work': 'Работать в госпитале',
              'bones_to_skeleton': 'Создать скелета',
              'to_farmer': 'Искать кости',
              'to_defer': 'Охрана дома',
              'to_attacker': 'В наступление'}
    Error = {'no_energy': 'Не хватает энергии',
             'no_bones': 'Не хватает костей',
             'no_waiter': 'Нет свободных скелетов',
             'no_comands': 'Нет такой команды'}
    complite = {'kill_hum': f'Вы нашли бедалагу которого никто не вспомнит '
                            f'\n +{balance.bones_for_kill_human} костей',
                'work': f'После тяжелого рабочего дня '
                        f'\n +{balance.gold_for_work} золота',
                'bones_to_skeleton': f'Еще один прислужник ждет приказа'
                                     f'\n -{balance.skeleton_need_bones} костей',
                'to_farmer': 'Один скелет отправился в лес добыть кости',
                'to_defer': 'Один скелет отправился охранять дом',
                'to_attacker': 'Один скелет отправился готовится к наступлению'}
