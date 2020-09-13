n1 = int(input('Dígite um número. '))
n2 = int(input('Dígite outro número. '))
if n1 > n2:
    print('{} é maior que {}.'.format(n1,n2))
elif n1 < n2:
    print('{} é maior que {}.'.format(n2,n1))
else:
    print('Não existe valor maior.')