class Board:
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def show_table(self):
        print(" %s | %s | %s" % (self.board[0], self.board[1], self.board[2]))
        print("-----------")
        print(" %s | %s | %s" % (self.board[3], self.board[4], self.board[5]))
        print("-----------")
        print(" %s | %s | %s" % (self.board[6], self.board[7], self.board[8]))

    def _is_valid_move(self, cell_number):
        if self.board[cell_number] == " ":
            return True
        else:
            print("Это поле уже занято")
            return False

    def change_board(self, cell_number, sign):
        if self._is_valid_move(cell_number):
            self.board[cell_number] = sign
            return self.board
        else:
            return None

    def is_winner(self, player):
        if (
            self.board[0] == player
            and self.board[1] == player
            and self.board[2] == player
        ):
            return True
        if (
            self.board[3] == player
            and self.board[4] == player
            and self.board[5] == player
        ):
            return True
        if (
            self.board[6] == player
            and self.board[7] == player
            and self.board[8] == player
        ):
            return True
        if (
            self.board[0] == player
            and self.board[3] == player
            and self.board[6] == player
        ):
            return True
        if (
            self.board[1] == player
            and self.board[4] == player
            and self.board[7] == player
        ):
            return True
        if (
            self.board[2] == player
            and self.board[5] == player
            and self.board[8] == player
        ):
            return True
        if (
            self.board[0] == player
            and self.board[4] == player
            and self.board[8] == player
        ):
            return True
        if (
            self.board[2] == player
            and self.board[4] == player
            and self.board[6] == player
        ):
            return True
        return False

    def is_full(self):
        used_cell = 0
        for cell in self.board:
            if cell != " ":
                used_cell += 1
        if used_cell == 9:
            return True
        else:
            return False
