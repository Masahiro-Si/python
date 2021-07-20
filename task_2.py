# Создайте собственный класс-исключение, обрабатывающий ситуацию деления
# на нуль. Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.


# class MakeCalc:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         self._chk_num()
#
#     def _chk_num(self):
#         pass
#
#     def __str__(self):
#         return f'{self.__class__.__name__}: {self._chk_num()}'


class OwnError(Exception):
    pass


class CheckNumber:
    def chk_num(self):
        while True:
            try:
                self.a, self.b = input(
                    'Введите два числа через пробел для выполнения их деления: \n'
                    'Для завершения введите "stop": '
                    ).split(' ')
                return int(self.a) / int(self.b)
            except Exception as err:
                raise OwnError(f'Что то пошло не так, ваша ошибка:\n {err}')


if __name__ == '__main__':
    try:
        test = CheckNumber()
        print(test.chk_num())
    except OwnError as err:
        print(f'Ошибка ввода данных: {err}')
    except Exception as err:
        print(f'Непредвиденная ошибка: {err}')