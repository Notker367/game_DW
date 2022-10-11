from Model import roles, logic
import time


def key(user: roles.User, text: str):
    pass


def get_story(user: roles.User):
    return logic.get_story_from_stack(user.chat_id)


def set_story(user: roles.User, choice, part):
    story = get_story(user)

    story.choice += [choice]
    story.part = part


def check(story: roles.Story):
    part = story.part
    if part is 'story1':
        pass


def story1(story: roles.Story):
    pass


def story2(story: roles.Story):
    pass
