import random
from time import sleep

n = int(input('Entre 0 e 5, em que número eu pensei? '))
sorteio = random.randint(0, 5)

print('Processando...')
sleep(2)

if n == sorteio:
    print('Parabéns, você acertou!')
else:
    print('Você errou, eu pensei no {}'.format(sorteio))
