# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
# слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить
# только первые 10 букв в слове.
i = 1
user_str = input('Введите несколько слов разделенных пробелом: ')
for word in user_str.split(' '):
    print(f'{i}, {word[:10]}')
    i += 1
print(user_str)
print(type(user_str))
