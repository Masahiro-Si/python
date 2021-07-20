class ReadDataError(Exception):
    pass


class CheckUserInput:
    def __init__(self):
        self.new_list = []

    def num_input(self):
        while True:
            try:
                el = input('Введите целое число и нажмите Enter: ')
                if el == 'stop':
                    return f'Итоговый список: {self.new_list}'
                self.new_list.append(int(el))
            except Exception as err:
                raise ReadDataError(f'Введены некорректные данные.\n{err}')


if __name__ == '__main__':
    try:
        check = CheckUserInput()
        print(check.num_input())
    except ReadDataError as err:
        print(f'Ошибка ввода данных: {err}')
    except Exception as err:
        print(f'Непродвиденная ошибка: {err}')
