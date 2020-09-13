completa = list()
pares = list()
impar = list()
while True:
    completa.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar [S/N]: '))
    if r in 'Nn':
        break
for c in completa:
    if c % 2 == 0:
        pares.append(c)
    else:
        impar.append(c)
print('-=' * 30)
print(f'A lista completa é {completa}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpar é {impar}.')
