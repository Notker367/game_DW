import Necromant_class
import logic

user = Necromant_class.Necromant()

logic.me_info()

logic.wait(5)

logic.kill_human()
logic.kill_human()

logic.create_skeleton()

logic.skeleton_go_to('farmer')

logic.take_from_farm_bone(4)

logic.create_skeleton()

logic.skeleton_go_to('attacker')

logic.attack(0, 1)

logic.me_info()
