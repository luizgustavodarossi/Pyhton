num = int(input('Digite um número inteiro'))
print('Escolha uma base de conversão')
print('''[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif op == 2:
    print('{} convertido para OCTAL é igual {}'.format(num, oct(num)))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
