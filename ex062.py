print('='*25)
print('   10 termos de uma PA')
print('='*25)
pt = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão da PA: '))
termo = pt
cont = 1
fim = 0
mais = 10
while mais != 0:
    fim = fim + mais
    while cont <= fim:
        print(termo, end=' -> ')
        cont += 1
        termo += razao
    print('Pausa')
    mais = int(input('Quantos termos a mais você quer ver? '))
print('Progressão finalizada com {} termos'.format(cont-1))
