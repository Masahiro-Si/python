from time import sleep


class TrafficLight:
    def __init__(self, *color):
        self.__color_1, self.__color_2, self.__color_3 = color

    def running(self):
        while True:
            if self.__color_1 == 'red':
                print(self.__color_1)
                sleep(7)
            else:
                print('Не верный порядок цветов.\nЦвета светофора red, yellow, green')
                break
            if self.__color_2 == 'yellow':
                print(self.__color_2)
                sleep(2)
            else:
                print('Не верный порядок цветов.\nЦвета светофора red, yellow, green')
                break
            if self.__color_3 == 'green':
                print(self.__color_3)
                sleep(6)
            else:
                print('Не верный порядок цветов.\nЦвета светофора red, yellow, green')
                break


start = TrafficLight('red', 'yellow', 'green')
start.running()
