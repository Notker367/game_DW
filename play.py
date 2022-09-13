import db

user = db.get_user(727922443)

user.necromant = db.get_necromant(user)

print(user.necromant.bones)
