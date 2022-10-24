def fonction(*parametres):
    my_list = []
    for param in parametres:
        if isinstance(param,(int)):
            my_list.append(param)
        else:
            print("Ce n'est pas un nombre/chiffre")
    for elm in my_list:
        if elm % 2 == 0:
            print(elm)

fonction(1,3,6,16,23,46,48,53,54,70,80,77,43)