soma = mil = c = barato = 0
nome = ''

print('='*30)
print('     Lojão do Cagão')
print('='*30)
while True:
    prod = input('Nome do produto: ')
    preco = float(input('Preço: R$ '))
    soma += preco
    c += 1
    if c == 1:
        barato = preco
        nome = prod
    if preco < barato:
        barato = preco
        nome = prod
    if preco > 1000:
        mil += 1
    opcao = input('Quer continuar? [S/N] ').strip().lower()[0]
    if opcao == 'n':
        break
print('-----------Fim-----------')
print('O total da compra foi R$ {}'.format(soma))
print('Tem {} produtos que custam mais do que mil reais'.format(mil))
print('O produto mais barato foi {} que custa {} reais'.format(nome, barato))
