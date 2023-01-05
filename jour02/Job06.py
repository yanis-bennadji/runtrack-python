num1 = input('entrer un nombre : ')

def nombre(nombre):
    if nombre > 0 :
        print ("Positif")
    elif nombre < 0 :
        print ("Négatif")
    else :
        print ("Je suis le nombre 0")

nombre(float(num1))