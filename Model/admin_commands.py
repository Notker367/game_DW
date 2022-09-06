def cheats(necr, commads):
    commads = commads.split()
    if len(commads) <= 2:
        return
    if commads[1] == 'energy':
        necr.add_energy(int(commads[2]))
    elif commads[1] == 'bones':
        necr.add_bones(int(commads[2]))
    elif commads[1] == 'gold':
        necr.add_gold(int(commads[2]))
    elif commads[1] == 'level':
        necr.set_lvl(int(commads[2]))
    if len(commads) <= 3:
        return
    if commads[1] == 'skeletons':
        necr.set_skeletons(commads[2], int(commads[3]))
    else:
        print('Error cheats')
