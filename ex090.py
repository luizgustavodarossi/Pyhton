aluno = dict()
aluno['Nome'] = str(input('Nome:'))
aluno['Média'] = float(input(f'Média do {aluno["Nome"]}:'))
if aluno['Média'] >= 6:
    aluno['Situação'] = 'APROVADO'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
    aluno['Situação'] = 'REPROVADO'
print('-=' * 30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')