maior = 0
nome_v = ''
soma = 0
cont = 0

for i in range(1, 5):
    print('-'*4, '{}º pessoa'.format(i), '-'*4)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo(M/F): ').upper()
    soma += idade
    if sexo == 'M' and idade > maior:
        maior = idade
        nome_v = nome
    if sexo == 'F' and idade < 20:
        cont += 1

print('\nA média de idade do grupo é de {}'.format(soma/4))
print('O nome do homem mais velho é {}'.format(nome_v))
print('A quantidade de mulheres que têm menos de 20 anos é {}'.format(cont))
