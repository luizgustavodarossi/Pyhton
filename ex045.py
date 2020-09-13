from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas Opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if jogador == 0 or jogador == 1 or jogador == 2:
    print('=-=' * 10)
    print('''Computador jogou {}
    Jogador jogou {}'''.format(itens[computador], itens[jogador]))
    print('=-=' * 10)
if computador == 0:#computador jogou Pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador venceu!')
    elif jogador == 2:
        print('Computador venceu!')
    else:
        print('Jogada inválida')
elif computador == 1:#computador jogou Papel
    if jogador == 0:
        print('Computador venceu!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador venceu!')
    else:
        print('Jogada inválida')
elif computador == 2:#computador jogou Tesoura
    if jogador == 0:
        print('Jogador venceu!')
    elif jogador == 1:
        print('Computador venceu!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida')
