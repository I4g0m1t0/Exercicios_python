n = int(input('Digite um número: '))
cont = 0
p = ''
for c in range(1, n+1):
    if n % c == 0:
        print("\033[91m" + str(c), end=' ')
        cont += 1
    else:
        print("\033[97m" + str(c), end=' ')
if cont == 2 or cont == 1:
    p = 'é primo.'
else:
    p = 'não é primo.'
print("\033[m" + '\nO número digitado foi dividido inteiramente por {} números, portanto ele {}'.format(cont, p))
