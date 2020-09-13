from time import sleep
from random import randint

computador = randint(0, 5)  # Faz o Computador sortear um número aleatório
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que númeto eu pensei? '))
print('Processando....')
sleep(2)
if jogador == computador:
    print('Parabéns você venceu!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))
