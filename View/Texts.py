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
              'to_farmer': 'Разведка',
              'to_defer': 'Защита',
              'to_attacker': 'Атака',
              'necr_info': 'info-инвентарь',
              'necromancy': 'Некромантия',
              'skills': 'Навыки',
              'to_reset': 'Вернуть скелетов',
              'skel_work': 'Направить скелетов',
              'upgrade': 'Улучшения',
              'back': 'Назад',
              'up_basement': f'Расширить подвал',
              'up_chest': f'Купить сундук',
              'up_lvl': f'Заняться расшифровкой'
              }

    Error = {'no_energy': 'Не хватает энергии',
             'no_bones': 'Не хватает костей',
             'no_waiter': 'Нет свободных скелетов',
             'no_commands': 'Нет такой команды',
             'undefait': 'Воспользуйтесь клаивиатурой',
             'no_gold': 'Нужно больше золота',
             'undefait_no_user': 'Пользователь не найден, если хотите зарегистрироваться напишите /start'}

    complite = {'kill_hum': f'Вы нашли бедалагу которого никто не вспомнит '
                            f'\n +{balance.bones_for_kill_human} костей',
                'heal_hum': f'Получено вознаграждение после тяжелого рабочего дня'
                            f'\n +{balance.gold_for_work} золотых',
                'bones_to_skeleton': f'Еще один прислужник ждет приказа'
                                     f'\n -{balance.skeleton_need_bones} костей',
                'to_farmer': 'Cкелет отправился в лес добыть кости',
                'to_defer': 'Cкелет отправился охранять дом',
                'to_attacker': 'Cкелет отправился готовится к наступлению',
                'to_reset': 'Скелеты вернулись к вам в дом',
                'up_lvl_basement': 'Ваш подвал расширен',
                'up_lvl_chest': 'Вы купили еще сундук для хранения своего богатсва',
                'lvlup': 'Ваши знания некромантии возросли'
                }

    event_button = {'confirm': 'Понятненько!',
                    'start_attack': 'Начать атаку',
                    'cancel_attack': 'Отложить атаку'}

    event_text = {'def': 'Атака на дом',
                  'none': 'Ничего не произошло',
                  'attack': 'Отличное время для атаки. Хотите её начать?',
                  'skeletons_win': 'Скелеты победили',
                  'skeletons_lose': 'ti loh'}

    callback = {'create': 'Cоздан пользователь с id '}

    keyboards = {'main': 'Вы у себя дома',
                 'work': 'Вы нашли пациента, которого уже не спасти, что с ним делать?',
                 'necromancy': 'PIVO necromancy',
                 'skel_work_options': 'Решите как использовать ваших прислужников',
                 'upgrade': f'Сдесь вы можете купить полезные штучки\n(В некст патче ПИВО)'}

    skills = {'lvl0': 'вы еще не достойны пить pivo',
              'lvl1': 'вы можете выпить 1 pivo',
              'lvl2': 'вы можете выпить 2 pivo',
              'lvl3': 'вы можете выпить 3 pivo',
              'lvl4': 'вы можете выпить 4 pivo',
              'lvl5': 'вы можете выпить 5 pivo'}


class Story_text:
    story1 = {'story1 bla-bla'}
