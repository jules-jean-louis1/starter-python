val1 = int(input("Entrée une première valeur :"))
val2 = int(input("Entrée uns seconde valeur :"))
print("Valeur 1 :", val1)
print("Valeur 2 :", val2)


for i in range(val1+1,val2+1,++1):
    print(i)
for i in range(val1-1,val2,-1):
        print(i)
if val1 == val2:
    print("Valeur égales")

    
