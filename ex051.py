print('='*25)
print('   10 termos de uma PA')
print('='*25)
pt = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão da PA: '))
decimo = pt + 10 * razao
for c in range(pt, decimo, razao):
    print(c, end=' -> ')
