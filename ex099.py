from time import sleep
def maior(listaValores):
    for n, v in enumerate(listaValores):
        if n == 0:
            maior = v
        elif maior < v:
            maior = v
    interface(maior, listaValores)


def interface(m, l):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for i in l:
        print(i, end=' ')
        sleep(0.3)
    print(f'Foram informados {len(l)} valores ao todo.')
    print(f'O maior valor informado foi {m:.0f}')
    print('-=' * 30)


#Programa Principal
l = list()
qtd = int(input('Quantos valores quer comparar?'))

for c in range(0, qtd):
    l.append(float(input(f'Digite o {c+1}° valor: ')))
maior(l)
