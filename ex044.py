print('=-=' * 15)
print('             Loja Guanabara')
print('=-=' * 15)
valor = float(input('Dígite o valor da compra: '))
print('''Escolha a opção de pagamento
[ 1 ] a vista no dinheiro/cheque
[ 2 ] a vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Qual é a opção? '))
if op == 1:
    print('Sua compra de R${} vai custar R${} no final'.format(valor, valor * 0.9))
elif op == 2:
    print('Sua compra de R${} vai custar R${} no final'.format(valor, valor * 0.95))
elif op == 3:
    valor_parcela = valor / 2
    print('''Sua compra será parcelada em 2x de R${} SEM JUROS
    Sua compra permanecerá em R${}'''.format(valor_parcela, valor))
elif op == 4:
    parcela = int(input('Em quantas vezes deseja parcelar? '))
    valor_parcela = valor / parcela
    print('''Sua compra será parcelada em {}x de R${:.2f} COM JUROS
    Sua compra de R${} irá custar R${:.2f} no final'''.format(parcela, valor_parcela, valor, valor * 1.2))
else:
    print('Opção inválida')