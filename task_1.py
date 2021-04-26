def divizion(x, y):
    return x / y


a, b = list(map(int, input('Введите два положительных числа: ').split(' ')))
while b == 0:
    print('Деление на 0 невозможно!')
    b = int(input('Введите целое положительное число: '))
else:
    res = divizion(a, b)
    print(res)
