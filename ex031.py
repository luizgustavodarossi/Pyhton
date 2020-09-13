distance = int(input('Qual é a distância da sua viagem?'))
print('Você está prestes a começar uma viagem de {}km'.format(distance))
if distance <= 200:
    preco = distance * 0.50
else:
    preco  = distance * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preco))