from time import sleep
from random import randint
computador = 1
jogador = 0
cont = 0
while computador != jogador:
    computador = randint(0, 10) #Aleatório de 0 à 10
    print('-=-' * 20)
    print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
    print('-=-' * 20)
    jogador = -1
    while jogador < 0 or jogador > 10:
        jogador = int(input('Em que número eu pensei? '))
        if jogador < 0 or jogador > 10:
            print('Dígite uma valor válido! Entre 0 e 10.')
    print('PROCESSANDO...')
    sleep(1.5)
    cont += 1
    if computador != jogador:
        print('GANHEI! Pensei no número {} e não no {}.'.format(computador, jogador))
print('Parabéns você ganhou! Pensei em {} também. Você precisou de {} vez(es) para ganhar de mim'.format(computador, cont))
