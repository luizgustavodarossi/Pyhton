def cab():
    print('-=' * 30)
    print(f'{"Calcula área de terreno":-^60}')
    print('-=' * 30)
def leitura():
    l = float(input('Informe a largura do terreno em metros: '))
    c = float(input('Informe o comprimento do terreno em metros: '))
    area(l, c)
def area(lar, com):
    a = lar * com
    print(f'O Terreno com {lar:.1f} X {com:.1f} tem sua área total de {a:.1f} m2.')


cab()
leitura()
