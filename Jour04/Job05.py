L = [2,4,6,8,10]
print(L[1])
def remplacement(Liste):
    L_somme = Liste[2] + Liste[4] 
    Liste.insert(3,L_somme)
    print(Liste[3])
    print(L[5])
remplacement(L)