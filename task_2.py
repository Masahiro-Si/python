# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

count_words = 0
count_lines = 0
with open('task_2.txt', 'r') as f:
    for line in f:
        print(f' В строке {len(line.split())} слов(а)')
        count_lines += 1
    print(f' Всего строк в фале: {count_lines}')
