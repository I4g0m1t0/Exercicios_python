preco = float(input('Qual o valor da sua compra? R$'))
print('Formas de pagamento')
print('[1] à vista dinheiro/cheque')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
opcao = int(input('Qual a sua opção? '))

if opcao == 1:
    novo = preco * 0.9
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, novo))
elif opcao == 2:
    novo = preco * 0.95
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, novo))
elif opcao == 3:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, preco))
elif opcao == 4:
    novo = preco * 1.20
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, novo))
else:
    print('Selecione uma opção válida!')