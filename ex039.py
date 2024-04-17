from datetime import date

ano = int(input('Ano em que você nasceu: '))
anoAtual = date.today().year

if (anoAtual - ano) < 18:
    print('Esse ainda não é o seu ano de alistamento, faltam {} anos'.format(18 - (anoAtual - ano)))
elif (anoAtual - ano) == 18:
    print('Você deve se alistar esse ano!')
elif (anoAtual - ano) > 18:
    print('Você deveria ter se alistado há {} anos'.format(anoAtual - ano - 18))
