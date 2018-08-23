y = int(input('введите год '))

if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print('високосный год')
        else:
            print('обычный год')
    else:
        print('високосный год')
else:
    print('обычный год')

