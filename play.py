import logic

user = logic.create_user()

logic.kill_human(user)

'''
logic.wait(5)

logic.kill_human(user)
logic.kill_human()

logic.create_skeleton()

logic.skeleton_go_to('farmer')

logic.take_from_farm_bone(4)

logic.create_skeleton()

logic.skeleton_go_to('attacker')

logic.attack(0, 1)
'''
print(logic.user_info(user))


