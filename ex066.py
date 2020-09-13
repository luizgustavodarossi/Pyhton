cont = 0
soma = 0
while True:
    n = int(input('Dígite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} vezes. A soma dos números digitados foi de {soma}')
