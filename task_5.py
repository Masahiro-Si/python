class ComplexNumber:
    def __init__(self, a, b=0):
        self.__complex = complex(a, b)

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            other = other.__complex
        return ComplexNumber(self.__complex + other)

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            other = other.__complex
        return ComplexNumber(self.__complex * other)

    def __str__(self):
        return f'{self.__complex}'


if __name__ == '__main__':
    test_1 = ComplexNumber(1, 2)
    test_2 = ComplexNumber(3)
    test_3 = ComplexNumber(3, 2)
    print(test_1 + test_2 + test_3)
    print(test_1 * test_2 * test_3)
