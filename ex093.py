jogador = dict()
partidas = list()
totalGols =0
jogador['Nome'] = str(input('Nome do Jogador: '))
npartidas = int(input('Quantas partidas jogadas: '))
for i in range(0, npartidas):
    partidas.append(int(input(f'Quantidade de gols na {i+1}° jogo: ')))
    totalGols += partidas[i]
jogador['Gols'] = partidas[:]
jogador['Total'] = totalGols
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {npartidas} partidas.')
for n, g in enumerate(partidas):
    print(f'=> Na {n+1}° partida, fez {g} gol(s).')
print(f'totalizando {totalGols} gols ao todo.')
