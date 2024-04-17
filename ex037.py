n = int(input('Digite um número inteiro: '))
print('[1] para converter para binário')
print('[2] para converter para octal')
print('[3] para converter para hexadecimal')
opcao = int(input('Sua opção: '))
if opcao == 1 :
    print('Esse número convertido para binário fica {}'.format(bin(n)[2:]))
elif opcao == 2:
    print('Esse número convertido para octal fica {}'.format(oct(n)[2:]))
elif opcao == 3:
    print('Esse número convertido para hexadecimal fica {}'.format(hex(n)[2:]))
else:
    print('Opção inválida')