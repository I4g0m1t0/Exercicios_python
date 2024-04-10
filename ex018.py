import math

ang = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O valor do seno desse ângulo é: {:.2f}'.format(seno))
print('O valor do cosseno desse ângulo é: {:.2f}'.format(cos))
print('O valor da tangente desse ângulo é: {:.2f}'.format(tan))
