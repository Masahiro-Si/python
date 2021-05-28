# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open('task_1.txt', 'w') as text_file:
    user_input = True
    while user_input:
        user_input = input('Введите данные: ')
        text_file.write(user_input + '\n')


with open('task_1.txt', 'r') as text_file:
    for line in text_file:
        print(line, end='')
