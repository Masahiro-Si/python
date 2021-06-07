def int_func(text):
    new_text = []
    for word in text.split(' '):
        new_text.append(word.capitalize())
    return ' '.join(new_text)


first_text = 'fIrSt'
print(int_func(first_text))

# user_text = input('Введите несколько слов из латинских букв разделенных пробелом: ')
user_text = "First second's third"
print(int_func(user_text))
