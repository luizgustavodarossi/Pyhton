while True:
    print('-' * 40)
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if tabuada < 0:
        break
    else:
        for c in range(0, 10):
            print(f'{tabuada} X {c+1} = {tabuada * (c+1)}')
