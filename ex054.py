from datetime import datetime
a = 0
c = 0

for i in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))
    if datetime.today().year - ano >= 18:
        a += 1
    else:
        c += 1
print('A quentidade de pessoas maiores de idade é igual a: {}'.format(a))
print('A quentidade de pessoas menores de idade é igual a: {}'.format(c))
