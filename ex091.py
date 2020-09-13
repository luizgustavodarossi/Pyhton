from random import randint
from time import sleep
from operator import itemgetter
game = {'Jogador1': randint(1, 6), 'Jogador2': randint(1, 6), 'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6)}
print('Valores sorteados')
print('--' * 15)
ranking = list()
for j, d in game.items():
    print(f'O {j} tirou: {d} no dado.')
    sleep(1)
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
print('-=' * 15)
print('Ranking dos jogadores')
print('-=' * 15)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar {v[0]} com {v[1]}.')