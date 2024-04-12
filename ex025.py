'''nome = input('Digite o seu nome: ').strip()

baixo = nome.lower()

silva = baixo.find('silva')

if silva>0 :
    print('Tem')
else:
    print('Não tem')'''

nome = input('Digite o seu nome: ').strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))