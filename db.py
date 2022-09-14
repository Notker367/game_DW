import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from Model import roles
import config

# Use a service account.
cred = credentials.Certificate(config.sA_link)

app = firebase_admin.initialize_app(cred)

db = firestore.client()

# links
c_users = db.collection('users')


def c_world(user_id):
    return c_users.document(user_id).collection('world')


def check_chat_id(chat_id):
    if type(chat_id) is int:
        chat_id = str(chat_id)
    return chat_id


def set_user(user: roles.User):
    chat_id = check_chat_id(user.chat_id)
    doc = c_users.document(chat_id)
    doc.set(user.to_dict())


def get_user(chat_id):
    chat_id = check_chat_id(chat_id)
    doc = c_users.document(chat_id)
    doc = doc.get()
    if not doc.exists:
        return False
    user_info = doc.to_dict()
    user = roles.User.from_dict(user_info)
    return user


def set_necromant(user: roles.User, necr: roles.Necromant):
    chat_id = check_chat_id(user.chat_id)
    doc = c_world(chat_id).document('Necromant')
    doc.set(necr.to_dict())


def get_necromant(user: roles.User):
    chat_id = check_chat_id(user.chat_id)
    doc = c_world(chat_id).document('Necromant')
    doc = doc.get()
    if not doc.exists:
        return False
    necr_info = doc.to_dict()
    necr = roles.Necromant.from_dict(necr_info)
    return necr


def save(user: roles.User, necr: roles.Necromant):
    set_user(user)
    set_necromant(user, necr)


def load(chat_id):
    user = get_user(chat_id)
    if not user:
        return False, False
    necr = get_necromant(user)
    return user, necr
