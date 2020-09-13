c = 'S'
cont = 0
soma = 0
while c =='S':
    n = int(input('Digite um número: '))
    soma += n
    c = str(input('Quer continuar? [S/N]')).upper()
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
media = soma / cont
print('''Você digitou {} vezes, e a média foi {:.2f}.
O maior valor foi {} e o menor {}.'''.format(cont, media, maior, menor))
