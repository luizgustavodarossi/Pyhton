numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor duplicado, Não vou adicionar.')
    r = str(input('Quer continuar [S/N]: ').lower())
    if r in 'n':
        break
numeros.sort()
print('-' * 30)
print(f'Os valores digitados foram {numeros}')
