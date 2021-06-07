def divizion(x, y):
    while y == 0:
        print('Деление на 0 невозможно!')
        y = int(input('Введите целое положительное число: '))
    else:
        return print(x / y)


a, b = list(map(int, input('Введите два положительных числа: ').split(' ')))
divizion(a, b)
