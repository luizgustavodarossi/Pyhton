from datetime import date
nascimento = int(input('Em que ano você nasceu? '))
atual = date.today().year
alistamento = nascimento + 18
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, atual - nascimento, atual))
if alistamento == atual:
    print('Você tem que se alistar IMEDIATAMENTE!!!.')
elif (alistamento > atual):
    print('Ainda faltam {} anos para você se alistar'.format(alistamento - atual))
    print('Seu alistamento será em {}'.format(alistamento))
else:
    print('Você já deveria ter se alistado há {} anos.'.format(atual - alistamento))
    print('Seu alistamento foi em {}'.format(alistamento))
