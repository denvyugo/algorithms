a = int(input('введите целое число '))
b = int(input('введите целое число '))
c = int(input('введите целое число '))

mn = a
mx = a
if b > mx:
    mx = b
if c > mx:
    mx = c
if b < mn:
    mn = b
if c < mn:
    mn = c
if mn < a < mx:
    print(f'среднее число: {a}')
elif mn < b < mx:
    print(f'среднее число: {b}')
else:
    print(f'среднее число: {c}')
