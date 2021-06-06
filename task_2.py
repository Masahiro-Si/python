class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.road_weight = 25
        self.road_thickness = 5

    def calc(self):
        try:
            int(self._length)
            int(self._width)
        except Exception as e:
            print(f'wrong length and width values,\n{e}')
        else:
            print(f'Масса асфальта: {(self._length * self._width * self.road_weight * self.road_thickness) / 1000} т.')


# test = Road('word', 20)
# test.calc()
test_2 = Road(5000, 20)
test_2.calc()
