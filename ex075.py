lista = [int] * 5
for c in range(0, 5):
    lista[c] = int(input(f'Digite o {c + 1}° número: '))
tupla = (lista[0], lista[1], lista[2], lista[3], lista[4])
print(f'Você digitou: {tupla}')
print(f'Apareceu {tupla.count(9)} vezes o númeiro 9.')
if tupla.count(3) != 0:
    print(f'A primeira posição que se encontra o número 3 é a posição {tupla.index(3) + 1}')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')
print('Os númeiros pares foram: ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')
