numeros = [[], []]
for c in range(0, 7):
    leitura = (int(input('Dígite um número: ')))
    if leitura % 2 == 0:
        numeros[0].append(leitura)
    else:
        numeros[1].append(leitura)
numeros[0].sort()
numeros[1].sort()
print('-=' * 30)
print(f'Os números pares digitados foram:{numeros[0]}\nOs números ímpares digitados foram:{numeros[1]}')
