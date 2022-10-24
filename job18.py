def fonction(*params):
    my_list = []

    for param in params:
        if isinstance(param,(int)):
            my_list.append(param)
            my_list.sort()
        else:
            print("Ce n'est pas un nombre/chiffre")
    print(my_list)

fonction(1,3,6,16,23,46,48,53,54,70,80,77,43)