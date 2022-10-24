nombre= int(input("Entrer un nombre :"))

with open("data.txt", "r") as f:
    texte = f.read()

nb = 0
for ligne in texte:
    per_word = texte.split()
    for elm in per_word:
        if len(elm) == nombre:
            nb = nb +1

