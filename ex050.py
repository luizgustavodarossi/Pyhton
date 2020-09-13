s = 0
for c in range(0, 6):
    n = int(input('Dígite um número: '))
    if n % 2 == 0:
        s += n
print('A soma de todos os números pares digitados foi de {}'.format(s))
