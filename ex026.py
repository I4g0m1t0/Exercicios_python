frase = input('Digite uma frase: ').strip()
baixo = frase.lower()
cont = baixo.count('a')
primeira = baixo.find('a')
ultimo = baixo.rfind('a')
print('A letra A apareceu {} vezes'.format(cont))
print('A letra A apareceu primeiro na posição {}'.format(primeira+1))
print('A letra A apareceu por último na posição {}'.format(ultimo+1))