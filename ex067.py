while True:
    valor = int(input('Digite um número para ver sua tabuada: '))
    print('-' * 40)
    if valor < 0:
        break
    elif valor >= 0:
        for i in range(1, 11):
            print('{} x {} = {}'.format(valor, i, valor * i))
    print('-' * 40)
print('Programa encerrado!')
