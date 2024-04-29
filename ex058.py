import random
from time import sleep
c = 0
n = int(input('Entre 0 e 5, em que número eu pensei? '))
c += 1
sorteio = random.randint(0, 5)

print('Processando...')
sleep(2)

while n != sorteio:
    n = int(input('Você errou! Tente novamente: '))
    c += 1
    print('Processando...')
    sleep(1)
print('Parabéns, você acertou na {}ª tentativa!'.format(c))
