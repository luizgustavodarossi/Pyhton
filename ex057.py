sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe seu sexo [M/F]: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Inválido!!')
if sexo =='M':
    print('Masculino')
else:
    print('Feminino')
