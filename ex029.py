vel = float(input('Em que velocidade o seu carro está agora? '))
limite = 80

if vel > limite:
    multa = (vel - limite)*7
    print('Multado! Por exceder o limite de velocidade de 80km/h você deverá pagar R${:.2f}'.format(multa))
else:
    print('Dirija com segurança!')
