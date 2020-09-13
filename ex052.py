n = int(input('Dígite um número: '))
d = 0
for c in range(1, n + 1):
    if n % c == 0:
        d = d + 1
print('O número {} foi divisivel {} vezes.'.format(n, d))
if d == 2:
    print('O número {} é primo.'.format(n))
else:
    print('O número {} não é primo.'.format(n))
