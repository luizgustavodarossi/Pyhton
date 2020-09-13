frase = str(input('Dígite uma frase')).strip()
print('A letra A aparece {} vezes a frase'.format(frase.lower().count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.lower().find('a')+1))
print('A última letra A apareceu na posição {}'.format(frase.lower().rfind('a')+1))
