lista= list()
jogador = dict()
partidas = list()
print(f'{"FUTEBOL":*^55}')
while True:
    jogador.clear()
    partidas.clear()
    print('-' * 55)
    jogador['Nome'] = str(input('Nome do Jogador: '))
    npartidas = int(input('Quantas partidas jogadas: '))
    for i in range(0, npartidas):
        partidas.append(int(input(f'Quantidade de gols na {i+1}° jogo: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    lista.append(jogador.copy())
    while True:
        res = str(input('Quer continuar?[S/N]: ').upper()[0])
        if res in 'SN':
            break
        print('Erro! Resposta Inválida')
    if res == 'N':
        break
print(lista)
print('-=' * 30)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('--' * 30)
for k, v in enumerate(lista):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('--' * 30)
while True:
    buscar = int(input('Mostrar dados de qual jogador?'))
    if buscar == -1:
        break
    if buscar >= len(lista):
        print(f'Erro! Não existe jogador com o cod {buscar}!')
    else:
        print('--' *30)
        print(f'LEVANTAMENTO DO JOGADOR')
        print(f'Nome do Jogador: {lista[buscar]["Nome"]}')
        for i, g in enumerate(lista[buscar]['Gols']):
            print(f'Na {i+1}° partida, fez {g} gols.')

