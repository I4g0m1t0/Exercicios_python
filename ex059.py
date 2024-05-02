from time import sleep

opcao = 0

while opcao != 5:
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    print('   [ 1 ] somar')
    print('   [ 2 ] multiplicar')
    print('   [ 3 ] maior')
    print('   [ 4 ] novos números')
    print('   [ 5 ] sair')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('{} x {} = {}'.format(n1, n2, n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print(n1)
        if n2 > n1:
            print(n2)
    elif opcao == 4:
        print('Informe os números novamente')
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida, tente novamente')
print('Fim do programa')
