

from cmd import PROMPT
h = "Bonjour"
b = "Au revoir"

while True:
    var1 = str(input('>'))
    if var1 == h:
        print("Bonjour a toi")
    elif var1 == b:
        print("Au revoir")
        break
    else:
        print(var1)
        