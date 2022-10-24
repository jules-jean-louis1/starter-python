from itertools import permutations


def sort(liste):
    premutation = True
    passage = 0
    while premutation == True:
        premutation = False
        passage = passage + 1
        for encours in range (0, len(liste) - passage):
            if liste [encours] > liste [encours +1]:
                permutations = True
                liste[encours], liste[encours+1]=\
                liste[encours+1],liste[encours]
    return liste

def Display(liste2):
    print(liste2)

Display(sort([5,8,85,26,78,50]))