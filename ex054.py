from datetime import date
maior = 0
menor = 0
atual = date.today().year
for c in range(0, 7):
    idade = int(input('Em que ano a {}° pessoa nasceu? '.format(c+1)))
    if (atual - idade) >= 18:
        maior += 1
    else:
        menor += 1
print('''Ao todo tivemos {} maiores de idade.
E também tivemos {} menores de idade'''.format(maior, menor))
