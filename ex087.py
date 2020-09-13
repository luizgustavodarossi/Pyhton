matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol =  0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Dígite um número para a posição [{i},{j}]: '))
print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            spar += matriz[i][j]
    print()

for l in range(0, 3):
    scol += matriz[l][2]
    if l == 0:
        mai = matriz[1][l]
    elif matriz[1][l] > mai:
        mai = matriz[1][l]
print('-=' * 30)
print(f'A soma dos valores pares é de {spar}')
print(f'A soma dos valores da terceira coluna é de {scol}')
print(f'O maior valor da segunda linha é {mai}')