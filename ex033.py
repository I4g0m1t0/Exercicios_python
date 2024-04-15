n1 = float(input('Primeiro valor: '))
maior = n1
menor = n1
n2 = float(input('Segundo valor: '))
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2
n3 = float(input('Terceiro valor: '))
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))
