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



'''
# set
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})
______________________________________________________
# get
users_ref = db.collection(u'users')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
'''


def add_user(user: roles.User):
    doc = c_users.document(str(user.chat_id))
    doc.set({
        'chat_id': user.chat_id,
        'name': user.name,
        'username': user.username,
        'create_time': user.create_time
    })


def get_user(chat_id):
    doc = c_users.document(str(chat_id)).get()
    if not doc.exists():
        return False
    user_info = doc.to_dict()
    user = roles.User(user_info.get('chat_id'),
                      user_info.get('name'),
                      user_info.get('username'),
                      user_info.get('create_time'),
                      )
    return user


def set_necromant(chat_id: str, necr: roles.Necromant):
    doc = c_world(chat_id).document('Necromant')
    doc.set({
        'energy': necr.energy,
        'bones': necr.bones,
        'gold': necr.gold,
        'level': necr.level,
        'keyboard': necr.keyboard,
        'skeletons': necr.skeletons,
        'cd_event': necr.cd_event
    })
