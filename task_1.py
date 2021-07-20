from abc import ABC


class DataError(Exception):
    pass


class Date(ABC):
    def __init__(self):
        self._data = None



    @classmethod
    def int_method(cls, text):
        print([int(el) for el in text.split('-')])

    @staticmethod
    def valid_method(text):
        date = text.split('-')

        try:
            len(date) == 3
        except Exception as e:
            raise DataError(f'Не точное количесво данных\n{e}')

        try:
            int(date[0]) in range(1, 31)
        except Exception as e:
            raise DataError(f'Не правильно указан день.\nОшибка:{e}\n')

        try:
            int(date[1]) in range(1, 12)
        except Exception as e:
            raise DataError(f'Не правильно указан месяц.\nОшибка:{e}\n')

        try:
            int(date[2]) in range(0, 2021)
        except Exception as e:
            raise DataError(f'Не правильно указан год.\nОшибка:{e}\n')

        return date


if __name__ == '__main__':
    try:
        i = Date()
        i.int_method('12-07-2021')
        Date.int_method('13-07-2021')
        v = Date()
        print(v.valid_method('15-07-2021'))
        print(v.valid_method('day-month-year'))
        print(v.valid_method('40-15'))
    except DataError as err:
        print(f'ошибка ввода данных: {err}')
    except Exception as err:
        print(f'Непредвиденная ошибка: {err}')
