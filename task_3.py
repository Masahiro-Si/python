class Worker:
    def __init__(self, wage, bonus):
        self.name = None
        self.surname = None
        self.position = ''
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        if not self.name:
            print(f'Имя сотрудника не указано. {self.name}')
        elif not self.surname:
            print(f'Фамилия сотрудника не указана. {self.surname}')
        else:
            print(f'Полное имя сотрудника: {self.name} {self.surname}.')

    def get_total_income(self):
        try:
            print(f'Доход сотрудника: {sum(self._income.values())}\n')
        except TypeError as e:
            print(f'Не вернно указан доход или премия, \nпроверьте правильность ввода.\n{e}')


worker_1 = Position(10000, 5000)
worker_1.name, worker_1.surname = 'Peter', 'Hobs'
worker_1.get_full_name()
worker_1.get_total_income()

worker_2 = Position('word', 3000)
worker_2.name, worker_2.surname = 'Robbert', 'Palmer'
worker_2.get_full_name()
worker_2.get_total_income()

worker_3 = Position(19000, 3000)
worker_3.get_full_name()
worker_3.get_total_income()

worker_4 = Position(5000, 8000)
worker_4.name = 'Gilbert'
worker_4.get_full_name()
worker_4.get_total_income()
