from Model import roles, balance, story_block
from View import keyboards, bot_send, callbacks
from View.Texts import Text_for, Story_text
import db

user_list = {}
'''
{'<chat_id>:   {'user': User,
                'necr': Necromant,
                'story': Story
                }
}
'''
request_text = {}
users_time = {}
need_event = False

main_options = ['info_necr',
                'work',
                'necromancy', 'upgrade']

work_options = ['kill_hum',
                'heal_hum']

necromancy_options = ['bones_to_skeleton',
                      'to_farmer', 'to_defer', 'to_attacker',
                      'to_reset',
                      'back']

upgrade_options = ['up_basement',
                   'up_chest',
                   'up_lvl',
                   'back']

story_options = {'continue_story',
                 'skip_story',
                 'continue'}


def key_check(options, text, user):
    if back_key(user, text):
        main_keyboard(user)

    elif set(options).issubset(main_options):
        main_key(user, text)

    elif set(options).issubset(work_options):
        work_key(user, text)

    elif set(options).issubset(necromancy_options):
        necromancy_key(user, text)

    elif set(options).issubset(upgrade_options):
        upgrade_key(user, text)

    elif set(options).issubset(story_options):
        story_block.key(user, text)

    else:
        undefait_text(user)


def add_user_stack(user: roles.User, necr: roles.Necromant, story: roles.Story):
    chat_id = try_type(user.chat_id)

    new_user = {'user': user,
                'necr': necr,
                'story': story}
    user_list.update({chat_id: new_user})
    print(f'Добавлен пользователь в стак - {new_user}')
    welcome(user)


def get_user_from_stack(chat_id):
    chat_id = try_type(chat_id)
    user = user_list.get(chat_id)['user']
    return user


def get_necr_from_stack(chat_id):
    chat_id = try_type(chat_id)
    necr = user_list.get(chat_id)['necr']
    return necr


def get_story_from_stack(chat_id):
    chat_id = try_type(chat_id)
    story = user_list.get(chat_id)['story']
    return story


def registration(message):
    print(f'registration user {message.chat.id}')
    chat = message.chat

    chat_id = chat.id
    name = chat.first_name

    if chat.last_name:
        name += " " + chat.last_name
    username = chat.username
    create_time = message.date

    add_new_user(chat_id, name, username, create_time)


def add_new_user(chat_id, name, username, create_time):
    options = ['continue_story', 'skip_story']
    new_user = roles.User(chat_id=chat_id,
                          name=name,
                          username=username,
                          create_time=create_time,
                          necromant=roles.Necromant(keyboard=options)
                          )
    new_necr = new_user.necromant
    new_story = roles.Story()

    db.set_user(new_user)
    db.set_necromant(new_user, new_necr)
    db.set_story(new_user, new_story)

    bot_send.message(new_user, Story_text.story0)

    add_user_stack(new_user, new_necr, new_story)


def welcome(user: roles.User):
    options = get_active_keyboard(user)

    if not options:
        keyboard = keyboards.keyboard_create(main_options, user)
        set_active_keyboard(user, main_options)

    else:
        keyboard = keyboards.keyboard_create(options, user)
    bot_send.update_keyboard(user, callbacks.text_welcome(user), keyboard)


def get_active_keyboard(user: roles.User):
    necr = get_necr_from_stack(user.chat_id)
    options = necr.get_keyboard()
    return options


def set_active_keyboard(user: roles.User, options):
    necr = get_necr_from_stack(user.chat_id)
    necr.set_keyboard(options)


def get_user(chat_id):
    chat_id = try_type(chat_id)

    if chat_id in user_list:
        user_from_stack = get_user_from_stack(chat_id)
        print(f'User {chat_id} on stack')
        return user_from_stack

    user_from_db, necr_from_db, story_from_db = db.load(chat_id)
    if user_from_db:
        print(f'User {chat_id} on DB')
        add_user_stack(user_from_db, necr_from_db, story_from_db)
        print(f'Add user {chat_id} in stack')
        return user_from_db

    else:
        return False


def kill_human(necr: roles.Necromant):
    necr.take_energy()
    necr.add_bones(balance.bones_for_kill_human)


def heal_hum(me):
    me.take_energy()
    me.add_gold(balance.gold_for_work)


def create_skeleton(necr: roles.Necromant):
    # me.take_energy(1)
    necr.take_bones(balance.skeleton_need_bones)
    necr.set_skeletons('waiter', 1)


def skeleton_go_to(necr: roles.Necromant, work, count=1):
    """Ввести из farmer defer attacker"""
    if work not in necr.skeletons:
        print('Error skeleton_go_to type')
    necr.set_skeletons('waiter', count * -1)
    necr.set_skeletons(work, count)


def take_from_farm_bone(me, dif_time=1):
    farm_bone(me, dif_time)


def farm_bone(me, iteration=1):
    me.bones += me.skeletons.get('farmer') * 5 * iteration


def event_attack(me):
    guards = 1
    skeletons = me.skeletons.get('attacker')
    lost = fight(guards, skeletons, balance.win_skels_change_attack)
    guards_lost, skeletons_lost = lost[0], lost[1]
    skeletons_death = skeletons - skeletons_lost
    after_fight = (guards - guards_lost) * balance.bones_for_kill_guard \
                  + skeletons_death * balance.bones_for_kill_skeleton
    skeletons_win = lost[0] == 0
    if skeletons_win:
        me.add_bones(after_fight)
        if balance.roll() <= balance.change_read_book:
            me.lvlup()
    me.set_skeletons('attacker', skeletons_death * -1)
    return Text_for.event_text['skeletons_win'] if skeletons_win \
        else Text_for.event_text['skeletons_lose']


def event_def(me, rouges=1):
    def_skels = me.skeletons.get('defer')
    lost = fight(rouges, def_skels, balance.win_skels_change_def)
    after_fight = rouges - lost[0] * balance.bones_for_kill_rouge \
                  + def_skels - lost[1] * balance.bones_for_kill_skeleton
    me.set_skeletons('defer', (def_skels - lost[1]) * -1)
    skeletons_win = lost[0] == 0
    if skeletons_win:
        me.add_bones(after_fight)
    else:
        me.take_gold(lost[0] * balance.gold_for_rouge)


def fight(units, skels, win_skels_change):
    """
    Битва пока кого-то не станет 0

    :param units: Кол-во противников
    :param skels: Кол-во скелетов
    :param win_skels_change: Шанс что выграет скилет 1 на 1 с units в %
    :return: list[units, skels]
    """
    bg = [units, skels]
    while not (0 in bg):
        if balance.roll() <= win_skels_change:
            bg[0] -= 1
        else:
            bg[1] -= 1
    return bg


def time_step(me, time):
    try:
        prew_time = users_time[me.chat_id]
    except:
        users_time[me.chat_id] = time
        return
    d_time = time - prew_time
    step_energy(me, d_time)
    check_event(me, d_time)
    users_time[me.chat_id] = time


def check_event(me, time):
    global need_event
    if me.cd_event <= 0:
        me.cd_event = balance.event_cd
        need_event = True
    else:
        me.cd_event = me.cd_event - time
        need_event = False


def step_energy(user, time):
    necr = db.get_necromant(user)
    need_add_energy = time // balance.time_for_add_energy
    energy_after = user.necromant.energy + need_add_energy
    if energy_after > balance.max_energy:
        necr.energy = balance.max_energy
    elif energy_after <= balance.max_energy:
        necr.add_energy(need_add_energy)
    else:
        print('Error logic step_energy')


def energy_add(me, count=1):
    me.add_energy(count)


def user_info(user):
    bot_send.message(user, user.info())


def energy_check(necr: roles.Necromant, need_energy=1):
    if necr.energy >= need_energy:
        have_energy = True
    else:
        have_energy = False
    return have_energy


def skeleton_waiter_check(necr: roles.Necromant, need_waiter=1):
    if necr.skeletons['waiter'] >= need_waiter:
        return True
    else:
        return False


def bones_check(me, need_bones):
    if me.bones >= need_bones:
        return True
    else:
        return False


def gold_check(necr: roles.Necromant, need_gold):
    if necr.gold >= need_gold:
        return True
    else:
        return False


def active_buttons(user):
    necr = db.get_necromant(user)
    return necr.get_keyboard()


def not_have_commands(user):
    bot_send.message(user, Text_for.Error['no_commands'])


def why_event(me):
    roll_event = balance.roll()
    attackers = me.skeletons['attacker']
    if roll_event <= balance.event_def_roll \
            and me.gold >= balance.gold_for_def_event:  # def_event
        rouges = balance.roll(0, (me.gold // balance.gold_for_rouge))
        event_def(me, rouges)
        return Text_for.event_text['def'], keyboards.keyboard_inline_create(['confirm'])
    elif roll_event <= balance.event_attack_roll \
            and attackers >= balance.need_attackers_for_attack_event:  # attack event
        return Text_for.event_text['attack'], keyboards.keyboard_inline_create(['attack'])
    else:
        return Text_for.event_text['none'], None


def admin_command(user, text):
    if text == '/admin':
        bot_send.message(user, Text_for.admin)
    else:
        text = text.split()
        if len(text) == 3:
            if text[1] == 'energy':
                user.add_energy(int(text[2]))
            elif text[1] == 'bones':
                user.add_bones(int(text[2]))
            elif text[1] == 'gold':
                user.add_gold(int(text[2]))
            elif text[1] == 'level':
                user.set_lvl(int(text[2]))
            else:
                bot_send.message(user, 'huity napisal')
        elif len(text) == 4:
            if text[1] == 'skeletons':
                user.set_skeletons(text[2], int(text[3]))
            else:
                bot_send.message(user, 'huity napisal')
        else:
            bot_send.message(user, 'Не верное количество аргументов')


def user_info_db(chat_id):
    user = db.get_user(chat_id)
    bot_send.message(user, str(user.to_dict()))


def main_key(user, text):
    necr = get_necr_from_stack(user.chat_id)

    have_energy = energy_check(necr)

    if text == Text_for.button['info_necr']:
        bot_send.message(user, callbacks.info_necr(necr))

    elif text == Text_for.button['work']:
        if have_energy:
            work_keyboard(user)
        else:
            story_step(user)
            bot_send.message(user, Text_for.Error.get('no_energy'))

    elif text == Text_for.button['necromancy']:
        necromancy_keyboard(user, necr)

    elif text == Text_for.button['upgrade']:
        bot_send.message(user, Text_for.keyboards.get('upgrade'))
        upgrade_keyboard(user, necr)

    else:
        undefait_text(user)


def upgrade_keyboard(user, necr):
    options = upgrade_options
    keyboard = keyboards.keyboard_create(options, user)
    bot_send.update_keyboard(user, callbacks.upgrade_text(necr), keyboard)
    set_active_keyboard(user, options)


def work_keyboard(user):
    options = work_options
    keyboard = keyboards.keyboard_create(options, user)
    bot_send.update_keyboard(user, Text_for.keyboards.get('work'), keyboard)
    set_active_keyboard(user, options)


def necromancy_keyboard(user, necr):
    options = necromancy_options
    keyboard = keyboards.keyboard_create(options, user)
    bot_send.update_keyboard(user, callbacks.necromancy_text(necr), keyboard)
    set_active_keyboard(user, options)


def back_key(user, text):
    necr = get_necr_from_stack(user.chat_id)

    if text == Text_for.button.get('back') and 'back' in necr.get_keyboard():
        return True
    else:
        return False


def upgrade_key(user, text):
    up_basement = text == Text_for.button.get('up_basement')
    up_chest = text == Text_for.button.get('up_chest')
    up_lvl = text == Text_for.button.get('up_lvl')

    necr = get_necr_from_stack(user.chat_id)

    have_gold_for_basement = gold_check(necr, balance.gold_for_buy_up_basement)
    have_gold_for_chest = gold_check(necr, balance.gold_for_buy_up_chest)
    have_gold_for_lvl = gold_check(necr, balance.gold_for_buy_up_lvl)

    if up_basement and have_gold_for_basement:
        buy_basement(necr)
        bot_send.message(user, Text_for.complite['up_lvl_basement'])

    elif up_chest and have_gold_for_chest:
        buy_chest(necr)
        bot_send.message(user, Text_for.complite['up_lvl_chest'])

    elif up_lvl and have_gold_for_lvl:
        buy_lvl(necr)
        bot_send.message(user, Text_for.complite['lvlup'])

    elif up_basement or up_chest or up_lvl:
        bot_send.message(user, Text_for.Error.get('no_gold'))

    upgrade_keyboard(user, necr)


def buy_lvl(necr):
    necr.take_gold(balance.gold_for_buy_up_lvl)
    necr.lvlup()


def buy_chest(necr):
    necr.take_gold(balance.gold_for_buy_up_chest)
    necr.up_lvl_chest()


def buy_basement(necr):
    necr.take_gold(balance.gold_for_buy_up_basement)
    necr.up_lvl_basement()


def work_key(user, text):
    necr = get_necr_from_stack(user.chat_id)
    have_energy = energy_check(necr)

    need_kill_hum = text == Text_for.button['kill_hum']
    need_heal_hum = text == Text_for.button['heal_hum']

    if need_kill_hum and have_energy:
        kill_human(necr)
        bot_send.message(user, Text_for.complite['kill_hum'])

    elif need_heal_hum and have_energy:
        heal_hum(necr)
        bot_send.message(user, Text_for.complite['heal_hum'])

    elif (need_heal_hum or need_kill_hum) and not have_energy:
        bot_send.message(user, Text_for.Error['no_energy'])

    main_keyboard(user)


def main_keyboard(user):
    options = main_options
    keyboard = keyboards.keyboard_create(options, user)
    bot_send.update_keyboard(user, Text_for.keyboards.get('main'), keyboard)
    set_active_keyboard(user, options)


def necromancy_key(user, text):
    # skills = text == Text_for.button['skills']
    skel_create = text == Text_for.button['bones_to_skeleton']
    back = text == Text_for.button['back']

    necr = get_necr_from_stack(user.chat_id)

    have_bones_for_create = bones_check(necr, balance.skeleton_need_bones)

    # if skills:
    #   bot_send.message(user, callbacks.skills(necr))

    if skel_create and have_bones_for_create:
        create_skeleton(necr)
        bot_send.message(user, Text_for.complite['bones_to_skeleton'])

    elif skel_create and not have_bones_for_create:
        bot_send.message(user, Text_for.Error['no_bones'])

    else:
        skel_work_key(user, text)

    necromancy_keyboard(user, necr)


def skel_work_key(user, text):
    to_farmer = text == Text_for.button['to_farmer']
    to_defer = text == Text_for.button['to_defer']
    to_attacker = text == Text_for.button['to_attacker']
    to_reset = text == Text_for.button['to_reset']

    necr = get_necr_from_stack(user.chat_id)

    have_waiter = skeleton_waiter_check(necr)

    if (to_farmer or to_defer or to_attacker) and not have_waiter:
        bot_send.message(user, Text_for.Error['no_waiter'])

    elif to_reset:
        skeleton_to_reset(necr)
        bot_send.message(user, Text_for.complite['to_reset'])

    elif to_farmer and have_waiter:
        skeleton_go_to(necr, 'farmer')
        bot_send.message(user, Text_for.complite['to_farmer'])

    elif to_defer and have_waiter:
        skeleton_go_to(necr, 'defer')
        bot_send.message(user, Text_for.complite['to_defer'])

    elif to_attacker and have_waiter:
        skeleton_go_to(necr, 'attacker')
        bot_send.message(user, Text_for.complite['to_attacker'])


def skeleton_to_reset(necr):
    all_skeletons = necr.get_all_skeletons()
    necr.skeletons = {'waiter': all_skeletons,
                      'farmer': 0,
                      'defer': 0,
                      'attacker': 0}


def undefait_text(user):
    necr = get_necr_from_stack(user.chat_id)
    actual_keyboard = necr.get_keyboard()

    if actual_keyboard:
        keyboard = keyboards.keyboard_create(actual_keyboard, user)
    else:
        keyboard = keyboards.keyboard_create(['start'])

    bot_send.update_keyboard(user, Text_for.Error['undefait'], keyboard)


def undefait_text_no_user(message):
    print(f'Пользователь {message.chat.id} не найден, неизвестный текст: {message.text}')
    keyboard = keyboards.keyboard_create(['start'])
    bot_send.update_keyboard_no_user(message, Text_for.Error['undefait_no_user'], keyboard)


def try_type(chat_id):
    if chat_id is not str:
        chat_id = str(chat_id)
    return chat_id


def save_from_stack_to_db():
    users = user_list.keys()
    print(users)
    for user in users:
        chat_id = user
        user = get_user_from_stack(chat_id)
        necr = get_necr_from_stack(chat_id)
        story = get_story_from_stack(chat_id)
        db.save(user, necr, story)
        print(f'Пользователь {user.chat_id} сохранен')
    print('Все пользователи сохранены')


def view_stack():
    print(user_list)


def story_step(user: roles.User):
    chat_id = user.chat_id
    story = get_story_from_stack(chat_id)

    story_block.check(story)
