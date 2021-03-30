# time = input('Введите время в секндах: ')
my_time = '12328'
my_time = int(my_time)
hours = my_time // 3600
minutes = (my_time % 3600) // 60
seconds = (my_time % 3600) % 60
print(f'Точное время: {hours:02d}:{minutes:02d}:{seconds:02d}')
print('Точное время: %d:%d:%d' % (hours, minutes, seconds))
print('Точное время: {}:{}:{}'.format(hours, minutes, seconds))
