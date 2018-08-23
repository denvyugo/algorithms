x1 = int(input('введите x коортинату первой точки '))
y1 = int(input('введите y коортинату первой точки '))
x2 = int(input('введите x коортинату второй точки '))
y2 = int(input('введите y коортинату первой точки '))
k = (y1 - y2) / (x1 - x2)
b = y1 - k * x1
if k != 0:
    if b != 0:
        if b<0:
            s = '-'
        else:
            s = '+'
        
        if k == 1:
            print(f'уравнение прямой y = x {s} {abs(b)}')
        else:
            print(f'уравнение прямой y = {k}x {s} {abs(b)}')
    else:
        if k == 1:
            print(f'уравнение прямой y = x')
        else:
            print(f'уравнение прямой y = {k}x')
else:
    print(f'уравнение прямой y = {b}')
