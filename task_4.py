# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.

translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('task_4.txt', 'r') as f:
    new_text = []
    for i in f:
        i = i.split(' ', 1)
        new_text.append(translator[i[0]] + ' ' + i[1])
    print(new_text)

with open('task_4_1.txt', 'w') as new_file:
    new_file.writelines(new_text)
