peso = float(input('Informe o seu peso (kg): '))
altura = float(input('Informe a sua altura (m): '))
imc = peso / altura**2
print('O seu IMC é de {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está raquítico')
elif imc < 25:
    print('Peso ideal!')
elif imc < 30:
    print('Você está em sobrepeso')
elif imc < 40:
    print('Você é obeso')
elif imc > 40:
    print('Você está no nível Thaís Carla, parabéns!')
