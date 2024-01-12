from unittest import TestCase

from game_handler import GameBoard, get_computer_input, get_user_input
from min_max_algo import MinMaxAlgorithm


class TestTicTacToe(TestCase):

    def test_validate_min_max(self):
        board = GameBoard()
        user_input = get_user_input()
        min_max_algo = MinMaxAlgorithm(board)
        i = 0
        while i < 3:
            for j in range(3):
                if not board.is_valid_move([i, j], user_input):
                    continue
                board.move([i, j], user_input)
                if board.check_winner()[0] or board.is_full():
                    break
                min_max_algo.min_max_solver()
                if not board.is_valid_move(min_max_algo.best_move, get_computer_input()):
                    self.assertTrue(False)
                    break
                board.move(min_max_algo.best_move, get_computer_input())

                if board.check_winner()[0] or board.is_full():
                    break
            if board.check_winner()[0] or board.is_full():
                break
            i += 1

        if board.check_winner()[0]:
            self.assertEquals(board.check_winner()[-1], get_computer_input())
        elif board.is_full():
            self.assertTrue(True)
        else:
            self.assertTrue(False)
