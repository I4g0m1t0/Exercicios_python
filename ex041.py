from datetime import date

ano = int(input('Ano de nascimento do atleta: '))
idade = date.today().year - ano
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Classificação: Mirim')
elif 14 >= idade > 9:
    print('Classificação: Infantil')
elif 19 >= idade > 14:
    print('Classificação: Júnior')
elif 25 >= idade > 19:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')
