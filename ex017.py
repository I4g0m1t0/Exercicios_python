import math

catop = float(input('Informe o valor do cateto oposto: '))
catad = float(input('Informe o valor do cateto adjacente: '))
hipot = (math.pow(catop, 2)) + (math.pow(catad, 2))
print('O valor da hipotenusa é: {}'.format(math.sqrt(hipot)))
