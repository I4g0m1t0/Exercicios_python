import random
cont = 0

print('='*30)
print('  Vamos jogar par ou ímpar?')
print('='*30)
while True:
    v = int(input('Diga um valor: '))
    opcao = input('Par ou ímpar? [P/I] ').strip().lower()
    print('-'*50)
    comp = random.randint(1, 10)
    soma = v + comp
    if soma % 2 == 0:
        resultado = 'deu par'
    else:
        resultado = 'deu ímpar'
    print('Você jogou {} e o computador {}. Total de {} {}'.format(v, comp, soma, resultado))
    print('-' * 50)
    if opcao == 'p' and resultado == 'deu par':
        print('Você ganhou')
        cont += 1
        print('Vamos jogar denovo...')
        print('-' * 50)
    elif opcao == 'i' and resultado == 'deu ímpar':
        print('Você ganhou')
        cont += 1
        print('Vamos jogar denovo...')
        print('-' * 30)
    else:
        print('Você perdeu')
        break
print('='*30)
print('GAME OVER! Você venceu {} vezes'.format(cont))