dias = float(input('Durante quantos dias o carro ficou alugado? '))
km = float(input('Quantos quilômetros o carro rodou enquanto estava alugado? '))
td = dias * 60
tkm = km * 0.15
print('O valor final a pagar ficou R${:.2f}'.format(td+tkm))
