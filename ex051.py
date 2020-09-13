t = int(input('Informe o termo da progressão aritmétrica: '))
r = int(input('Informe a razão da progressão aritmétrica: '))
d = t + (10 - 1) * r
for c in range(t, d, r):
    print('{}'.format(c), end=' - ')
print('FIM!')
