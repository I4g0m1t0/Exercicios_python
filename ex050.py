soma = 0

for c in range(0, 6):
    n = int(input('Digite o {}° número: '.format(c+1)))
    if n % 2 == 0:
        soma += n
print('A soma apenas dos números pares que você digitou é {}'.format(soma))
