num = int(input('Dígite um número: '))
fatorial = 1
c = num
while c > 0:
    fatorial *= c
    c -= 1
print('Fatorial de {}! é igual a {}.'.format(num, fatorial))
