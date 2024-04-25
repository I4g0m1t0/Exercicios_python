s = 0
c = 0

for i in range(1, 500, 2):
    if i % 3 == 0:
        s += i
        c += 1

print('Entre 1 e 500, existem {} valores ímpares, e a soma dos mesmos é igual a: {}'.format(c, s))
