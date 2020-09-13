n = int(input('Dígite um número da tabuada: '))
f = int(input('Deseja multiplica-ló até: '))
for c in range(0, f+1):
    print('{} X {} = {}'.format(n, c, n*c))
