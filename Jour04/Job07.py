L = [8, 24,48,2,16]

def multiple(Liste):
    i=0
    nb_multiple=0
    for i in Liste:
        if i % 3 == 0:
            nb_multiple = nb_multiple + 1
        else:
            continue
    print(nb_multiple)

multiple(L)
