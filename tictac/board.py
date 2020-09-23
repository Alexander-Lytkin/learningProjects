class Board:
    def __init__(self):
        self._board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def show_table(self):
        print(
            " %s | %s | %s" % (self._board[1], self._board[2], self._board[3])
        )
        print("-----------")
        print(
            " %s | %s | %s" % (self._board[4], self._board[5], self._board[6])
        )
        print("-----------")
        print(
            " %s | %s | %s" % (self._board[7], self._board[8], self._board[9])
        )

    def _is_valid_move(self, cell_number):
        if self._board[cell_number] == " ":
            return True
        else:
            print("Это поле уже занято")
            return False

    def change_cell(self, cell_number, sign):
        if self._is_valid_move(cell_number):
            self._board[cell_number] = sign
            return self._board
        else:
            return None

    def is_winner(self, player):
        if (
            self._board[1] == player
            and self._board[2] == player
            and self._board[3] == player
        ):
            return True
        if (
            self._board[4] == player
            and self._board[5] == player
            and self._board[6] == player
        ):
            return True
        if (
            self._board[7] == player
            and self._board[8] == player
            and self._board[9] == player
        ):
            return True
        if (
            self._board[1] == player
            and self._board[4] == player
            and self._board[7] == player
        ):
            return True
        if (
            self._board[2] == player
            and self._board[5] == player
            and self._board[8] == player
        ):
            return True
        if (
            self._board[3] == player
            and self._board[6] == player
            and self._board[9] == player
        ):
            return True
        if (
            self._board[1] == player
            and self._board[5] == player
            and self._board[9] == player
        ):
            return True
        if (
            self._board[3] == player
            and self._board[5] == player
            and self._board[7] == player
        ):
            return True
        return False

    def is_full(self):
        used_cell = 1
        for cell in self._board:
            if cell != " ":
                used_cell += 2
        if used_cell == 10:
            return True
        else:
            return False
