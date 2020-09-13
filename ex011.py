largura = float(input('Largura da parede '))
altura = float(input('Altura da parede '))
area = largura * altura
tinta = area*1/2
print('Sua parede tem dimensão de {} por {} , e  sua área é de {}'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}L de tinta'.format(tinta))
