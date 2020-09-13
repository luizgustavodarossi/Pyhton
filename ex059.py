op = 1
while op != 0:
    n1 = float(input('Digite o 1° número: '))
    n2 = float(input('Dígite o 2° número: '))
    op = int(input('''  MENU
    [1] SOMAR
    [2] MULTIPLICAR
    [3] SUBTRAIR
    [4] DIVIDIR
    [5] MAIOR NÚMERO
    [6] NOVOS NÚMEROS
    [0] SAIR DO PROGRAMA
    : '''))
    if op != 0:
        if op == 1:
            print('O resultado da soma de {} + {} é igual a {}.'.format(n1, n2, n1 + n2))
        elif op == 2:
            print('O resultado de {} multiplicado por {} é igual  a {}.'.format(n1, n2, n1 * n2))
        elif op == 3:
            print('O resultado da subtração de {} - {} é igual a {}.'.format(n1, n2, n1 - n2))
        elif op == 4:
            print('O resultado de {} dividido por {} é igual a {}.'.format(n1, n2, n1 / n2))
        elif op == 5:
            if n1 > n2:
                print('O primeiro número {} é maior que o segundo {}.'.format(n1, n2))
            elif n2 > n1:
                print('O segundo número {} é maior que o primeiro {}.'.format(n2, n1))
            else:
                print('Os valores são iguais.')
print('FIM DO PROGRAMA')
