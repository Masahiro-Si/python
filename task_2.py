import random
# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].


def list_filter(numbers):
    new_list = []
    for num in numbers[1:]:
        if num > numbers[0]:
            new_list.append(num)
        numbers = numbers[1:]
    print(new_list)


my_list = []
for num in range(10):
    my_list.append(random.randint(0, 300))
print(my_list)
list_filter(my_list)
