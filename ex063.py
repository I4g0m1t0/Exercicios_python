print('=' * 25)
print('        Fibonacci')
print('=' * 25)
fim = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
cont = 3
if fim == 1:
    print(t1, '-> Fim')
elif fim == 2:
    print('{} -> {} -> Fim'.format(t1, t2))
else:
    print(t1, end=' -> ')
    print(t2, end=' -> ')
    while cont <= fim:
        t3 = t1 + t2
        print(t3, end=' -> ')
        t1 = t2
        t2 = t3
        cont += 1
    print('Fim')
