from Model import roles, logic
from View import Texts, bot_send

# story№ : [story_options,
#         main_options,
#         work_options,
#         necromancy_options,
#         upgrade_options]
available_buttons = {'story0': ['continue_story', 'skip_story'],
                     'story1': ['work',
                                'heal_hum'],
                     'story2': ['work',
                                'kill_hum'],
                     'story3': ['work', 'necromancy',
                                'heal_hum', 'kill_hum',
                                'back'],
                     'story4': ['work', 'necromancy',
                                'heal_hum', 'kill_hum',
                                'bones_to_skeleton', 'to_farmer',
                                'back'],
                     'story5': ['work', 'necromancy',
                                'heal_hum', 'kill_hum',
                                'bones_to_skeleton', 'to_farmer', 'to_defer',
                                'back'],
                     'story6': ['work', 'necromancy',
                                'heal_hum', 'kill_hum',
                                'bones_to_skeleton', 'to_farmer', 'to_defer', 'to_attacker',
                                'back']
                     }


def buttons_for_story(buttons, user):
    story = get_story(user)
    part = story.part

    new_buttons = []

    for button in buttons:
        if button in available_buttons[part]:
            new_buttons += [button]

    return new_buttons


def key(user: roles.User, text: str):
    story = get_story(user)
    part = story.part

    continue_story = text == Texts.Text_for.button['continue_story']
    skip_story = text == Texts.Text_for.button['skip_story']

    if part == 'story0':
        if continue_story:
            set_story(user, '0 continue_story', 'story1')
            bot_send.message(user, Texts.Story_text.story1)
            logic.main_keyboard(user)
        if skip_story:
            pass

    pass


def get_story(user: roles.User):
    return logic.get_story_from_stack(user.chat_id)


def set_story(user: roles.User, choice, part):
    story = get_story(user)

    story.choice += [choice]
    story.part = part


def check(story: roles.Story):
    part = story.part
    if part == 'story1':
        pass


def story1(story: roles.Story):
    pass


def story2(story: roles.Story):
    pass
