casa = float(input('Qual é o valor da casa? '))
salario = float(input('O valor do seu sálario? '))
tempo = int(input('Quantos anos deseja pagar? '))
parcelas = tempo * 12
valorparcela = casa /parcelas
print('O valor das parcelas será de R${:.2f}'.format(valorparcela))
if (salario * 0.3) < valorparcela:
    print('Orçamento NEGADO!!!')
else:
    print('Orçamento APROVADO!!!')
