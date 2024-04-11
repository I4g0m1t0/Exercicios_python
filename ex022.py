nome = input('Digite o seu nome: ')

upper = nome.upper()
lower = nome.lower()
length = len(nome) - nome.count(' ')
primeiro = nome.find(' ')
separa = nome.split()

print(upper)
print(lower)
print(length)
print(primeiro)
print(separa[0], len(separa[0]))