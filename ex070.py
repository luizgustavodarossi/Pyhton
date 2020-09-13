total = 0
mil = 0
produto_barato = ''
while True:
    print('===' * 20)
    print('LOJA DO GUANABARA')
    print('===' * 20)
    produto = str(input('Dígite o nome do produto: ')).strip()
    preco = float(input('Dígite o preço do produto: '))
    if produto_barato == '':
        produto_barato = produto
        preco_barato = preco
    elif preco < preco_barato:
        produto_barato = produto
        preco_barato = preco
    if preco >= 1000:
        mil += 1
    total += preco
    print('---' * 20)
    sair = ''
    while sair != 'S' and sair != 'N':
        sair = str(input('Quer continuar? [S/N]: ')).upper()
    if sair == 'N':
        break
print('=====Compra Finalizada=====')
print(f'''O total da compra foi de R${total:.2f}.
Temos {mil} produtos que custam mais de mil reais.
O produto mais barato é {produto_barato} que custa R${preco_barato:.2f}''')

