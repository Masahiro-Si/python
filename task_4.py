from random import randint


class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'Your {self.name} rides.')

    def stop(self):
        print(f'Your {self.name} stopped.')

    def turn(self, direction):
        print(f'Your {self.name} turned to {direction}')

    def show_speed(self):
        print(f'Your speed is {self.speed}\n')


class TownCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Your speed is {self.speed}, you have exceeded your driving speed!\n')


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Your speed is {self.speed}, you have exceeded your driving speed!\n')


class SportCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)


town_car = TownCar('Filder', 'grey', 80, False)
print(f'Your car is {town_car.name}, '
      f'your color is {town_car.color}, '
      f'your speed is {town_car.speed} and '
      f'your police status is {town_car.is_police}.')
town_car.go()
town_car.stop()
town_car.turn("east")
town_car.show_speed()

work_car = WorkCar('Track', 'black', 60, False)
print(f'Your car is {work_car.name}, '
      f'your color is {work_car.color}, '
      f'your speed is {work_car.speed} and '
      f'your police status is {work_car.is_police}.')
work_car.go()
work_car.stop()
work_car.turn("south")
work_car.show_speed()

sport_car = SportCar('Ferrari', 'red', 280, False)
print(f'Your car is {sport_car.name}, '
      f'your color is {sport_car.color}, '
      f'your speed is {sport_car.speed} and '
      f'your police status is {sport_car.is_police}.')
sport_car.go()
sport_car.stop()
sport_car.turn("west")
sport_car.show_speed()

police_car = PoliceCar('Lada_Granta', 'braun', 55, True)
print(f'Your car is {police_car.name}, '
      f'your color is {police_car.color}, '
      f'your speed is {police_car.speed} and '
      f'your police status is {police_car.is_police}.')
police_car.go()
police_car.stop()
police_car.turn("north")
police_car.show_speed()
