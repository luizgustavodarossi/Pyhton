from random import randint
vence = 0
while True:
    print('=-=' * 20)
    print(' VAMOS JOGAR PAR OU ÍMPAR')
    print('=-=' * 20)
    computador = randint(1, 10)
    jogador_numero = int(input('Diga o valor: '))
    jogador_escolha = str(input('Você quer PAR ou ÍMPAR [P/I]: ')).upper()
    if (computador + jogador_numero) % 2 == 0:
        res = 'P'
    else:
        res = 'I'
    print('---' * 20)
    print(f'Você jogou {jogador_numero} e o computador jogou {computador}. Total de {jogador_numero + computador} deu ', end='')
    if res == 'P':
        print('PAR')
    else:
        print('ÍMPAR')
    if res == jogador_escolha:
        print('VOCÊ VENCEU!')
        vence += 1
    else:
        break
print('---' * 20)
print('VOCÊ PERDEU!')
print(f'GAME OVER! Você venceu {vence} vezes')