for c in range(0, 5):
    peso = float(input('Peso da {}° pessoa: '.format(c+1)))
    if c == 0:
        pesado = peso
        leve = peso
    else:
        if pesado < peso:
            pesado = peso
        if leve > peso:
            leve = peso
print('''O maior peso lido foi {:.2f}.
E o menor peso lido foi {:.2f}.'''.format(pesado, leve))
