ficha = []
while True:
    nome = str(input('Dígite seu nome: '))
    not1 = float(input('Dígite a primeira nota: '))
    not2 = float(input('Dígite a segunda nota: '))
    media = (not1 + not2) / 2
    ficha.append([nome, [not1, not2], media])
    res = str(input('Quer continuar adicionando? [S/N]: '))
    if res in 'Nn':
        break
while True:
    print('-=' * 5, 'BOLETIM', '-=' * 5)
    print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
    for n, i in enumerate(ficha):
        print(f'{n:<4}{i[0]:<10}{i[2]:>8.1f}')
    opc = int(input('Deseja mostrar nota de qual aluno? (-1 encerra o programa): '))
    if opc == -1:
        print('Finalizado!!')
        break
    if opc <= (len(ficha)-1):
        print(f'As notas do aluno {ficha[opc][0]} foram :{ficha[opc][1]}')