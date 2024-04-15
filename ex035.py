n1 = int(input('Primeiro lado: '))
maior = n1
menor = n1

n2 = int(input('Segundo lado: '))
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2

n3 = int(input('Terceiro lado: '))
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3

if n1 != maior and n1 != menor:
    meio = n1
if n2 != maior and n2 != menor:
    meio = n2
if n3 != maior and n3 != menor:
    meio = n3

if menor + meio > maior:
    print('É possível fazer um triângulo')
else:
    print('Não é possível fazer um triângulo')

