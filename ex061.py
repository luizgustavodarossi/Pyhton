t = int(input('Informe o termo da progressão aritmétrica: '))
r = int(input('Informe a razão da progressão aritmétrica: '))
cont = 1
while cont <= 10:
    print('{}'.format(t), end=' - ')
    t += r
    cont += 1
print('FIM!')