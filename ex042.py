n1 = int(input('Primeiro lado: '))
n2 = int(input('Segundo lado: '))
n3 = int(input('Terceiro lado: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2 == n3:
        print('É possível fazer um triângulo equilátero')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('É possível fazer um triângulo isósceles')
    elif n1 != n2 and n2 != n3 and n1 != n3:
        print('É possível fazer um triângulo escaleno')
else:
    print('Não é possível fazer um triângulo')

