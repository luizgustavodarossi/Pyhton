person = list()
leitura = list()
mai = men = 0
while True:
    leitura.append(str(input('Dígite seu nome: ')))
    leitura.append(float(input('Dígite seu peso: ')))
    if len(person) == 0:
        mai = men = leitura[1]
    else:
        if leitura[1] > mai:
            mai = leitura[1]
        if leitura[1] < men:
            men = leitura[1]
    person.append(leitura[:])
    leitura.clear()
    res = str(input('Quer continuar?[S/N]'))
    if res in 'nN':
        break

print('-=' * 30)
print(f'Ao todo você cadastrou {len(person)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in person:
    if p[1] == mai:
        print(f'{p[0]}', end=', ')
print(f'\nO menor peso foi de {men}Kg. Peso de ', end='')
for p in person:
    if p[1] == men:
        print(f'{p[0]}', end=', ')
