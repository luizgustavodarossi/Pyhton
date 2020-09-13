def escreva(msg):
    tam = len(msg)
    print('~' * tam)
    print(f'{msg}')
    print('~' * tam)

while True:
    frase = str(input('Dígite uma frase: '))
    escreva(frase)
    while True:
        res = str(input('Continuar [S/N]:').upper())
        if res in 'SN':
            break
    if res in 'N':
        break