import asyncio
import random
from unittest import TestCase, IsolatedAsyncioTestCase

from game_handler import GameBoard, get_computer_input, get_user_input
from min_max_algo import MinMaxAlgorithm


async def async_method():
    while True:
        yield random.randint(1, 11)


class Test:

    def __await__(self):
        yield 1
        yield 2
        yield 3
        return 4


def async_test(f):
    def wrapper(*args, **kwargs):
        coro = asyncio.coroutine(f)
        future = coro(*args, **kwargs)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(future)

    return wrapper


class TestAsyncTicTacToe(IsolatedAsyncioTestCase):
    def test_response(self):
        result = asyncio.run(Test().__await__())
        print("Result ", result)


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
