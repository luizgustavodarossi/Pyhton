from math import hypot

oposto = float(input('Dígite o valor do cateto oposto: '))
adjacente = float(input('Dígite o valor do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
