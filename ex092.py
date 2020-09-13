from datetime import date
ano = date.today().year
pessoa = dict()
pessoa['Nome'] = str(input('Digite seu nome: '))
pessoa['Idade'] = (ano - (int(input('Dígite o ano de  nascimento: '))))
pessoa['CTPS'] = int(input('Carteira de trabalho:(0 não tem )'))
if pessoa['CTPS'] != 0:
    pessoa['Contratacao'] = int(input('Ano de Contratação:'))
    pessoa['Salario'] = float(input('Sálario:'))
    pessoa['Aposentadoria'] = (pessoa['Contratacao'] + 35) - (ano - pessoa['Idade'])
print('-=' * 30)
for k, v in pessoa.items():
    print(f'{k} : {v}')
