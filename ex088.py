from random import randint
from time import sleep
lista = list()
print('-=' * 30)
print(f'{"MEGA SENA":^60}')
print('-=' * 30)
quantj = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, quantj):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    sleep(1)
    print(f'Jogo n°{c+1}:{lista}')
    lista.clear()
