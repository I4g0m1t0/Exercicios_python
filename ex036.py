valor = float(input('Digite o valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Pra pagar em quantos anos? '))

prestacao = valor/ (anos*12)

print('Para pagar uma casa de {} em {} anos o valor da prestação será de {:.2f}'.format(valor, anos, prestacao))

if prestacao < salario*0.3:
    print('Empréstimo concedido')
else:
    print('Empréstimo negado')