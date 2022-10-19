l = int(input("Longeur :"))
h = int(input("Hauteur :"))

for j in range(h):
    for i in range(l):
        if i == 0 or i == l:
            print('|', end='')
        else:
            print(' ', end='')
        if j == 0 or j == h - 1:
            print("-", end='')
        else:
            print(' ', end='')
    print('|', end="")
    print()
