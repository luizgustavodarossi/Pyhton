print('=' * 30)
print('{:^30}'.format('BANCO GUANABARA'))
print('=' * 30)
valor = int(input('Quanto deseja sacar? R$'))
saque = valor
cedulas = [100, 0], [50, 0], [20, 0], [10, 0], [5, 0], [2, 0], [1, 0]
while saque >= cedulas[0][0]:
    saque -= cedulas[0][0]
    cedulas[0][1] += 1
if cedulas[0][1] > 0:
    print(f'Total de {cedulas[0][1]} cédulas  de R${cedulas[0][0]}')
while saque >= cedulas[1][0]:
    saque -= cedulas[1][0]
    cedulas[1][1] += 1
if cedulas[1][1] > 0:
    print(f'Total de {cedulas[1][1]} cédulas  de R${cedulas[1][0]}')
while saque >= cedulas[2][0]:
    saque -= cedulas[2][0]
    cedulas[2][1] += 1
if cedulas[2][1] > 0:
    print(f'Total de {cedulas[2][1]} cédulas  de R${cedulas[2][0]}')
while saque >= cedulas[3][0]:
    saque -= cedulas[3][0]
    cedulas[3][1] += 1
if cedulas[3][1] > 0:
    print(f'Total de {cedulas[3][1]} cédulas  de R${cedulas[3][0]}')
while saque >= cedulas[4][0]:
    saque -= cedulas[4][0]
    cedulas[4][1] += 1
if cedulas[4][1] > 0:
    print(f'Total de {cedulas[4][1]} cédulas  de R${cedulas[4][0]}')
while saque >= cedulas[5][0]:
    saque -= cedulas[5][0]
    cedulas[5][1] += 1
if cedulas[5][1] > 0:
    print(f'Total de {cedulas[5][1]} cédulas  de R${cedulas[5][0]}')
while saque >= cedulas[6][0]:
    saque -= cedulas[6][0]
    cedulas[6][1] += 1
if cedulas[6][1] > 0:
    print(f'Total de {cedulas[6][1]} cédulas  de R${cedulas[6][0]}')
print('=' * 30)
print('Volte sempre  ao BANCO GUANABARA! Tenha um ótimo dia!')
