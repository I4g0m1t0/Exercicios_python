p = w = c = 0

while True:
    print('='*30)
    print('     Cadastre uma pessoa')
    print('='*30)
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').strip().lower()[0]
    if idade > 17:
        p += 1
    if sexo == 'm':
        c += 1
    if idade < 20 and sexo == 'f':
        w += 1
    print('=' * 30)
    opcao = input('Quer continuar? [S/N] ').strip().lower()[0]
    if opcao == 'n':
        break
print('Fim')
print('Você cadastrou {} pessoas com mais de 18 anos'.format(p))
print('Você cadastrou {} homens'.format(c))
print('Você cadastrou {} mulheres com menos de 20 anos'.format(w))
