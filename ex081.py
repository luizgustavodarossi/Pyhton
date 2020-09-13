lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar [S/N]: '))
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos na lista.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
