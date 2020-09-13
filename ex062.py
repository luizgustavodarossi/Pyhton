print('-=-' * 10)
print(' GERADOR DE PA')
print('-=-' * 10)
pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
ter = pri
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -'.format(ter), end=' ')
        ter += raz
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('A progressão finalizada com {} termos mostrados.'.format(total))
