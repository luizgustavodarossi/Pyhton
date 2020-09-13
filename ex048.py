s = 0
for c in range(0, 500):
    if c % 2 != 0:
        if c % 3 == 0:
            s += c
print('A soma total é {}'.format(s))