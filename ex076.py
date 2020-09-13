listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochilha', 120.32, 'Canetas', 21.3, 'livro', 34.9)
print('-' * 35)
print(f'{"Listagem de Preços":^35}')
print('-' * 35)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<25}', end='')
    else:
        print(f'R${listagem[pos]: >7.2f}')
