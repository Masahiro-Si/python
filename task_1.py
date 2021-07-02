class Matrix:
    def __init__(self, my_list):
        self._my_list = my_list

    def __str__(self):
        return '\n'.join(map(str, self._my_list))

    def __add__(self, other):
        self._my_list = Matrix(list(map(sum, zip(*i))) for i in zip(self._my_list, other._my_list))
        return self._my_list


if __name__ == '__main__':
    m_1 = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
    m_2 = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
    m_3 = Matrix([[-4, 0, 5], [-3, 0, 8], [2, 7, -13], [25, 2, -7]])

    print(m_1)
    print(m_2)
    print(m_1 + m_2 + m_3)
