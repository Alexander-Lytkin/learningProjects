import sys

from tictac.board import Board
from tictac.gamer import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.player_1 = Player("X", self.board)
        self.player_2 = Player("O", self.board)

    def who_is_winner(self):
        if self.board.is_winner(player="X"):
            print("{} победил".format("X"))
            self.play_again()
        elif self.board.is_winner(player="O"):
            print("{} победил".format("O"))
            self.play_again()

    def check_if_board_is_full(self):
        if self.board.is_full():
            print("Ничья!")
            return self.play_again()

    @staticmethod
    def play_again():
        play = input("Играть ещё раз? ДА/НЕТ: ").upper()
        if play == "ДА":
            play_game()
        elif play == "НЕТ":
            print("Игра окончена")
            sys.exit()


def play_game():
    game = Game()
    game.board.show_table()
    while True:
        game.player_1.move()
        game.board.show_table()
        game.who_is_winner()
        game.check_if_board_is_full()
        game.player_2.move()
        game.board.show_table()
        game.who_is_winner()
        game.check_if_board_is_full()
