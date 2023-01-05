langage = input('Entrer votre langage de programmation sans majuscule: ')

def je_suis_quoi(langage):
    if langage == 'javascript':
        print('tu es un developpeur web')
    elif langage == 'python':
        print('tu es un developpeur IA')
    elif langage == 'java':
        print('tu es un developpeur logiciel')
    elif langage == 'reacts':
        print('tu es un developpeur mobile')
    else :
        print('un jour, je serai le meilleur developpeur...')

je_suis_quoi(langage)