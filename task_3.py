class Cell:
    def __init__(self, cells):
        self._cells = cells

    def __add__(self, other):
        return Cell(self._cells + other._cells)

    def __sub__(self, other):
        if self._cells > other._cells:
            return Cell(self._cells - other._cells)

        return f'Ошибка вычислеения.'

    def __mul__(self, other):
        return Cell(self._cells * other._cells)

    def __truediv__(self, other) -> object:
        return Cell(self._cells // other._cells)

    def __str__(self):
        return f'Количество ячеек в клетке: {self._cells}'

    def make_order(self, cll_order):
        warp = self._cells // cll_order
        rest = self._cells % cll_order
        return  '\n'.join(['*' * cll_order] * warp + (['*' * rest] if rest else []))


if __name__ == '__main__':
    # cell_1 = 10
    # cell_2 = 5
    cell_1 = Cell(5)
    cell_2 = Cell(10)
    cell_3 = Cell(15)
    print(cell_1)
    print(cell_2)
    print(cell_1 + cell_2 + cell_3)
    print(cell_2 - cell_1)
    print(cell_1 - cell_2)
    print(cell_1 * cell_2 * cell_3)
    print(cell_1 / cell_2)
    print(cell_3 / cell_1)
    print((cell_1 * cell_3).make_order(13))
