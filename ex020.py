import random

e1 = input('Primeira equipe: ')
e2 = input('Segunda equipe: ')
e3 = input('Terceira equipe: ')
e4 = input('Quarta equipe: ')

equipes = [e1, e2, e3, e4]

random.shuffle(equipes)

print('A ordem de apresentação é : {}'.format(equipes))
