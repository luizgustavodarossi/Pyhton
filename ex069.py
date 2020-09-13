maior_18 = 0
homens_cad = 0
mulheres_20 = 0
while True:
    print('===' * 20)
    print('CADASTRE UMA PESSOA')
    print('===' * 20)
    sexo = ''
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Informe o sexo [M/F]: ')).upper()
    idade = int(input('Informe sua idade: '))
    print('---' * 20)
    if idade > 18:
        maior_18 += 1
    if sexo == 'M':
        homens_cad += 1
    elif idade < 20:
        mulheres_20 += 1
    sair = ''
    while sair != 'S' and sair != 'N':
        sair = str(input('Quer continuar? [S/N]:')).upper()
    if sair == 'N':
        break
print('======FIM DO PROGRAMA======')
print(f'''Total de pessoas com mais de 18 anos: {maior_18}
Ao todo temos {homens_cad} homens cadastrados.
E temos {mulheres_20} mulher(es) com menor de 20 anos.''')
