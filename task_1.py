from time import sleep


class TrafficLight:
    def __init__(self):
        self._color = ['red', 'yellow', 'green']

    def running(self):
        while True:
            for light in self._color:
                if light == 'red':
                    print(light)
                    sleep(7)
                elif light == 'yellow':
                    print(light)
                    sleep(2)
                elif light == 'green':
                    print(light)
                    sleep(6)


start = TrafficLight()
start.running()
