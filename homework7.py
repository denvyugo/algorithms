a = int(input('введите длину отрезка a '))
b = int(input('введите длину отрезка b '))
c = int(input('введите длину отрезка c '))

if a < (b + c) and a > abs(b - c) and b < (a + c) and b > abs(a - c) and c < (a + b) and c > abs(a - b):
    if a == b == c:
        print('треугольник равносторонний')
    elif a == b or b == c or a == c:
        print('треугольник равнобедренный')
    else:
        print('треугольник разносторонний')
else:
    print('не треугольник')

