opcao = ''
cont = 0
soma = 0
maior = menor = 0
while opcao != 'n':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    opcao = input('Quer continuar? [S/N] ').lower().strip()
print('Você digitou {} números e a média foi {}'.format(cont, soma/cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
