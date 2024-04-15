km = float(input('Qual é a distância da sua viagem? '))
if km <= 200:
    valor = km * 0.5
    print('Sua viagem custará R${:.2f}'.format(valor))
else:
    valor = km * 0.45
    print('Sua viagem custará R${:.2f}'.format(valor))
