#!/usr/bin/env python
__author__ = "Luis Rueda"
__email__ = "userlerueda@gmail.com"
__status__ = "Development"

import sys
import os
import logging
from termcolor import colored

logger = logging.getLogger(__name__)
SCREEN_LOGGING_LEVEL = logging.CRITICAL


class Game:

    def __init__(self):
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        self.players = ["X", "O"]
        self.colors = {self.players[0]: "green",
                       self.players[1]: "red",
                       " ": "white"}
        self.win_options = (("00", "01", "02"),
                            ("10", "11", "12"),
                            ("20", "21", "22"),
                            ("00", "10", "20"),
                            ("01", "11", "21"),
                            ("02", "12", "22"),
                            ("00", "11", "22"),
                            ("20", "11", "02"))
        self.game_over = False
        self.turn = "X"
        self.position = {"A1": (0, 0),
                         "A2": (1, 0),
                         "A3": (2, 0),
                         "B1": (0, 1),
                         "B2": (1, 1),
                         "B3": (2, 1),
                         "C1": (0, 2),
                         "C2": (1, 2),
                         "C3": (2, 2)}
        self.winner = None
        self.logger = logger.getChild(self.__class__.__name__)

    def __str__(self):
        string_board = ("    A | B | C \n"
                        "  +-----------+\n"
                        "1 | {} | {} | {} |\n"
                        "  +-----------+\n"
                        "2 | {} | {} | {} |\n"
                        "  +-----------+\n"
                        "3 | {} | {} | {} |\n"
                        "  +-----------+\n"
                        )
        self.logger.info("winner :: {}".format(self.winner))
        self.logger.info("game_over :: {}".format(self.game_over))
        self.logger.info("turn :: {}".format(self.turn))
        return string_board.format(
            colored(self.board[0][0], self.colors[self.board[0][0]]),
            colored(self.board[0][1], self.colors[self.board[0][1]]),
            colored(self.board[0][2], self.colors[self.board[0][2]]),
            colored(self.board[1][0], self.colors[self.board[1][0]]),
            colored(self.board[1][1], self.colors[self.board[1][1]]),
            colored(self.board[1][2], self.colors[self.board[1][2]]),
            colored(self.board[2][0], self.colors[self.board[2][0]]),
            colored(self.board[2][1], self.colors[self.board[2][1]]),
            colored(self.board[2][2], self.colors[self.board[2][2]]))

    def _calculate_tictactoe(self, options, player):
        if self.board[int(options[0][0])][int(options[0][1])] == player and \
           self.board[int(options[1][0])][int(options[1][1])] == player and \
           self.board[int(options[2][0])][int(options[2][1])] == player:
            return True
        else:
            return False

    def _calculate_winner(self):
        for player in self.players:
            for options in self.win_options:
                if self._calculate_tictactoe(options, player):
                    self.game_over = True
                    self.winner = player
        self.logger.debug("Game over :: {}".format(self.game_over))
        self.logger.debug("Winner :: {}".format(self.winner))

    def move(self, position):
        try:
            a = self.position[position.upper()][0]
            b = self.position[position.upper()][1]
        except Exception as e:
            self.logger.error(e)
            return False
        if self.board[a][b] == " ":
            self.board[a][b] = self.turn
            self._calculate_winner()
            self.logger.debug("game_over :: {}".format(self.game_over))
            if self.game_over is False:
                if self.turn == "X":
                    self.turn = "O"
                elif self.turn == "O":
                    self.turn = "X"
            return True
        else:
            return False


def main():
    logger = logging.getLogger()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.setLevel(SCREEN_LOGGING_LEVEL)
    stream_handler.setLevel(SCREEN_LOGGING_LEVEL)
    game = Game()
    while game.game_over is False:
        os.system('clear')
        print(game)
        print("It is {}'s turn\n".format(game.turn))
        position = raw_input("What is your move? ")
        while game.move(position) is False:
            print("Position {} is not valid or is already been used!"
                  .format(position))
            position = raw_input("What is your move? ")
            # position = input("What is your move?")
    os.system('clear')
    print(game)
    print("There is a winner!")
    print("Winner is {}".format(game.winner))
    sys.exit(0)


if __name__ == "__main__":
    sys.exit(main())
