class Player:
    def __init__(self, sign, board):
        self._sign = sign
        self._board = board

    def __str__(self):
        return "игрок {}".format(self._sign)

    def move(self):
        cell_number = int(input(f"Игрок {self}. Введите число от 1 до 9: "))
        while int(cell_number):
            if int(cell_number) > 9 or int(cell_number) <= 0:
                print(
                    ValueError(
                        "Введено неверное значение. Повторите ввод повторно"
                    )
                )
                break
            else:
                return self._board.change_cell(cell_number, self._sign)
