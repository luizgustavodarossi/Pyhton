from random import randint
num_ale = (randint(0, 9999), randint(0, 9999), randint(0, 9999), randint(0, 9999), randint(0, 9999))
print('Os valores foram :', end=' ')
for n in num_ale:
    print(n, end=' ')
print(f'\nO maior valor foi {max(num_ale)}')
print(f'O menor valor foi {min(num_ale)}')
