largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))
area = largura * altura
print('A sua parede com dimensões {} x {} tem {}m² de área'.format(largura, altura, area))
print('Para pintá-la vocÊ vai precisar de {}l de tinta'.format(area/2))
