import sys

from bank.tests.board1 import Board
from bank.tests.gamer1 import Player


def play_again():
    play = input("Играть ещё раз? ДА/НЕТ: ").upper()
    if play == "ДА":
        play_game()
    elif play == "НЕТ":
        print("Игра окончена")
        sys.exit()


class Game:
    def __init__(self):
        self.player_1 = Player("X")
        self.player_2 = Player("O")
        self.board = Board()

    def display_board(self):
        self.board.show_table()

    def make_move(self, cell_number, sign):
        return self.board.change_board(cell_number, sign)

    def who_is_winner(self):
        if self.board.is_winner("X"):
            print("{} победил".format("X"))
            play_again()
        elif self.board.is_winner("O"):
            print("{} победил".format("O"))
            play_again()

    def check_if_board_is_full(self):
        if self.board.is_full():
            print("Ничья!")
            return play_again()


def play_game():
    game = Game()
    game.display_board()
    player_1 = game.player_1
    player_2 = game.player_2
    number = 5
    while number > 0:
        game.check_if_board_is_full()
        x_number = int(
            input("Игрок {}. Введите число от 0 до 8: ".format(player_1))
        )
        game.make_move(x_number, player_1.sign)
        game.display_board()
        game.who_is_winner()
        game.check_if_board_is_full()
        o_number = int(
            input("Игрок {}. Введите число от 0 до 8: ".format(player_2))
        )
        game.make_move(o_number, player_2.sign)
        game.display_board()
        game.who_is_winner()
