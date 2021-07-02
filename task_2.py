from abc import abstractmethod


class Clothes:
    def __init__(self):
        self._textile = None
        self._name = None

    @property
    def textile(self):
        if self._textile is None:
            self._calc_textile()
        return self._textile

    @abstractmethod
    def _calc_textile(self):
        pass

    def __add__(self, other):
        result = Clothes()
        result._textile = self._textile + other._textile
        return result

    def __str__(self):
        if self._name is None:
            return f'Всего ткани для {self.__class__.__name__}' \
               f' надо: {self.textile:.2f}'
        else:
            return f'Всего ткани для {self.__class__.__name__} ' \
                   f'с названием: "{self._name}" ' \
                   f'понадобится: {self.textile:.2f}'


class Coat(Clothes):
    def __init__(self, v):
        self._v = v
        super().__init__()

    def _calc_textile(self):
        self._textile = self._v * 2 + 0.3


class Suit(Clothes):
    def __init__(self, h):
        self._h = h
        super().__init__()

    def _calc_textile(self):
        self._textile = self._h / 6.5 + 0.5


if __name__ == '__main__':
    coat_1 = Coat(5)
    coat_1._name = 'Зимнее'
    print(coat_1)

    suit_1 = Suit(20)
    print(suit_1)

    print(coat_1 + suit_1)
