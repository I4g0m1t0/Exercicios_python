import random

print('----JOGO PEDRA, PAPEL OU TESOURA----')
print('Suas opções')
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')
opcao_usuario = int(input('Qual a sua opção? '))
opcao_computador = random.randint(0, 2)

if opcao_usuario and opcao_computador == 0:
    print('Deu empate, os dois escolheram a mesma coisa')
elif opcao_usuario and opcao_computador == 1:
    print('Deu empate, os dois escolheram a mesma coisa')
elif opcao_usuario and opcao_computador == 2:
    print('Deu empate, os dois escolheram a mesma coisa')
elif opcao_usuario == 0 and opcao_computador == 1:
    print('Eu venci, você escolheu pedra e eu papel')
elif opcao_usuario == 0 and opcao_computador == 2:
    print('Você ganhou, você escolheu pedra e eu tesoura')
elif opcao_usuario == 1 and opcao_computador == 2:
    print('Eu venci, você escolheu papel e eu tesoura')
elif opcao_usuario == 1 and opcao_computador == 0:
    print('Você ganhou, você escolheu papel e eu pedra')
elif opcao_usuario == 2 and opcao_computador == 0:
    print('Eu venci, você escolheu tesoura e eu pedra')
elif opcao_usuario == 2 and opcao_computador == 1:
    print('Você ganhou, você escolheu tesoura e eu papel')
else:
    print('Selecione uma opção válida!')
