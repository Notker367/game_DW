from Model import roles, logic
from View import Texts, bot_send
import time

# story№ : [story_options,
#         main_options,
#         work_options,
#         necromancy_options,
#         upgrade_options]
story2_options = {'story2_1': ['story2_heal',
                               'story2_kill'],
                  'story2_2': ['story2_skelet'],
                  'story2_3': ['story2_kill_doc',
                               'story2_call_doc']
                  }

available_buttons = {'story0': ['continue_story', 'skip_story'],
                     'story1': ['work',
                                'heal_hum'],
                     'story2': ['work',
                                'kill_hum'],
                     'story2_1': story2_options['story2_1'],
                     'story2_2': story2_options['story2_2'],
                     'story2_3': story2_options['story2_3'],
                     'story3': ['work', 'necromancy',
                                'heal_hum', 'kill_hum',
                                'bones_to_skeleton',
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
                                'back'],
                     'story_main': ['info_necr',
                                    'work', 'necromancy', 'upgrade',
                                    'heal_hum', 'kill_hum',
                                    'bones_to_skeleton', 'to_farmer', 'to_defer', 'to_attacker',
                                    'up_basement', 'up_chest', 'up_lvl',
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

    story2_heal = text == Texts.Text_for.button['story2_heal']
    story2_kill = text == Texts.Text_for.button['story2_kill']

    story2_skelet = text == Texts.Text_for.button['story2_skelet']

    story2_kill_doc = text == Texts.Text_for.button['story2_kill_doc']
    story2_call_doc = text == Texts.Text_for.button['story2_call_doc']

    if part == 'story0':
        if continue_story:
            set_story(user, '0 continue_story', 'story1')
            bot_send.message(user, Texts.Story_text.story1)
            logic.main_keyboard(user)
        if skip_story:
            set_story(user, '0 skip_story', 'story_main')
            bot_send.message(user, Texts.Story_text.story_main)
            logic.main_keyboard(user)
            logic.add_energy(user, 30)

    if part == 'story2_1':
        if story2_heal:
            set_story(user, '1 story2_2_heal', 'story2_2')
            bot_send.message(user, Texts.Story_text.story2_2_heal)
        if story2_kill:
            set_story(user, '1 story2_2_kill', 'story2_2')
            bot_send.message(user, Texts.Story_text.story2_2_kill)
        logic.story_keyboard(user, story2_options['story2_2'], Texts.Story_text.story2_2)

    if part == 'story2_2':
        if story2_skelet:
            set_story(user, '2 story2_skelet', 'story2_3')
            bot_send.message(user, Texts.Story_text.story2_3)
        if story2_kill_doc:
            set_story(user, '2 story2_skelet', 'story2_3')
            bot_send.message(user, Texts.Story_text.story2_3)
        logic.story_keyboard(user, story2_options['story2_3'], Texts.Story_text.story2_2)

    if part == 'story2_3':
        if story2_kill_doc:
            set_story(user, '3 story2_kill_doc', 'story0')
            bot_send.message(user, Texts.Story_text.story2_fail)
            story_fail(user)
        if story2_call_doc:
            set_story(user, '3 story2_call_doc', 'story3')
            bot_send.message(user, Texts.Story_text.story3)
            logic.main_keyboard(user)


def get_story(user: roles.User):
    return logic.get_story_from_stack(user.chat_id)


def set_story(user: roles.User, choice, part):
    story = get_story(user)

    story.choice += [choice]
    story.part = part


def check(story: roles.Story, user: roles.User):
    part = story.part
    if part == 'story1':
        # в этой части юзер знакомится с семьей некромантов,
        # его везут туда при выходе из дома по пути в госпиталь
        return story1(user)
    else:
        return False


def story_fail(user):
    logic.story_keyboard(user, logic.story_options, Texts.Story_text.story_fail)


def story1(user: roles.User):
    bot_send.message(user, Texts.Story_text.story1_1)

    story2(user)
    return True


def story2(user: roles.User):
    set_story(user, '0 next', 'story2')
    bot_send.message(user, Texts.Story_text.story2)

    set_story(user, '1 next', 'story2_1')
    logic.story_keyboard(user, story2_options['story2_1'], Texts.Story_text.story2_1)

    logic.add_energy(user, 1)
    return True
