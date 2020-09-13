from datetime import date
anoAtual = date.today().year
pessoas = dict()
lista = list()
while True:
    pessoas['Nome'] = str(input('Nome: ').strip())
    pessoas['Sexo'] = 'C'
    while pessoas['Sexo'] not in 'M' and pessoas['Sexo'] not in 'F' or pessoas['Sexo'] == '':
        pessoas['Sexo'] = str(input('Sexo [M/F]: ').upper())
        if pessoas['Sexo'] not in 'M' and pessoas['Sexo'] not in 'F':
            print('Erro! Resposta inválida.')
    pessoas['Nascimento'] = anoAtual + 1
    while pessoas['Nascimento'] > anoAtual or pessoas['Nascimento'] <= (anoAtual - 150):
        pessoas['Nascimento'] = int(input('Ano de nascimento:'))
        if pessoas['Nascimento'] > anoAtual or pessoas['Nascimento'] <= (anoAtual - 150):
            print('Erro! Resposta inválida.')
    lista.append(pessoas.copy())
    pessoas.clear()
    res = 'C'
    while res not in 'SN' or res == '':
        res = str(input('Continuar adicionado?[S/N]: ').upper())
        if res not in 'S' and res not in 'N':
            print('Erro! Resposta inválida.')
    if res in 'N':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(lista)} pessoas')
somaIdade = 0
for i in range(0, len(lista)):
    somaIdade += (anoAtual - lista[i]['Nascimento'])
mediaIdade = (somaIdade / len(lista))
print(f'A média de idade do grupo é de {mediaIdade:.1f} anos.')
print(f'As mulheres do grupo são: ', end='')
for i in range(0, len(lista)):
    if lista[i]['Sexo'] == 'F':
        print(f'{lista[i]["Nome"]}', end=' * ')
print()
for i in range(0, len(lista)):
    if (anoAtual - lista[i]['Nascimento']) > mediaIdade:
        print(f'{lista[i]["Nome"]} tem idade acima da média, ele tem {(anoAtual - lista[i]["Nascimento"])} anos.')