salario = float(input('Qual é o salário do funcionário? '))
if salario > 1250:
    aumento = salario * 1.10
else:
    aumento = salario * 1.15
print('O funcionário que recebia R${:.2f} passou a receber R${:.2f}'.format(salario, aumento))
