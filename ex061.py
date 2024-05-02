print('='*25)
print('   10 termos de uma PA')
print('='*25)
pt = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão da PA: '))
'''nono = pt + 8 * razao
decimo = pt + 9 * razao
print(pt, end=' -> ')
while pt != nono:
    pt += razao
    print(pt, end=' -> ')
print(decimo)'''
termo = pt
cont = 1
while cont <= 10:
    print(termo, end=' -> ')
    cont += 1
    termo += razao
print('Fim')
