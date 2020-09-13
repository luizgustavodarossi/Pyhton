def contador(i, f, p):
    for c in range(i, f, p):
        print(c, end=' ')


#Programa Principal
while True:
    ini = int(input('Digite o valor para o inicio: '))
    while True:
        fim = int(input('Digite o valor para o fim: '))
        if fim == ini:
            print('O valor final não pode ser o mesmo que do inicio.')
        else:
            break
    passo = int(input('Digite o valor para o passo: '))
    if ini > fim:
        fim -= 1
        if passo > 0:
            passo = passo * (-1)
        elif passo == 0:
            passo = -1
    else:
        fim += 1
        if passo < 0:
            passo = passo *(-1)
        elif passo == 0:
            passo = 1
    print('--' *30)
    contador(ini, fim, passo)
    print('--' * 30)
    while True:
        res = str(input('\nContinuar?[S/N]').upper())
        if res in 'SN':
            break
    if res in 'N':
        break
