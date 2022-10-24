from itertools import permutations


def fonction(*params):
    my_list = []

    for param in params:
        if isinstance(param,(int)):
            my_list.append(param)
        else:
            print("Ce n'est pas un nombre/chiffre")

    permutation = True
    passage = 0
    
    while permutation == True:
        permutation=False
        passage=passage+1

        for encours in range(0, len(my_list)-passage):
            if my_list[encours]> my_list[encours+1]:
                permutation=True
                my_list[encours], my_list[encours+1]=\
                my_list[encours+1],my_list[encours]
    print(my_list)

fonction(1,3,6,16,23,46,48,53,54,70,80,77,43)