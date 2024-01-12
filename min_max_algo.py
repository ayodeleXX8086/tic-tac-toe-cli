import sys
from game_handler import GameBoard, get_computer_input, get_user_input


class MinMaxAlgorithm:

    def __init__(self, board: GameBoard):
        self.board = board
        self.best_move = (-1, -1)
        self.move = get_computer_input()

    def min_max_solver(self):
        def __min_max_solver(computer, depth):
            """
            To discover the best move by the computer it is ideal for the computer try all moves, this move is then traversed in a graph
            structure using a  DFS, for each move the computer will simulate the user and computer playing different moves, it will then
            search for the path with the maximum possibility and the minimum possibility of the user winning.
            For each node traversal there are three terminal states Such as (1) Computer winning, (-1) Computer lost, (0) A tie.
            :param computer: player identity
            :param depth: depth of the decision tree.
            """
            is_winner_board, winner = self.board.check_winner()
            if is_winner_board:
                return 1 if winner == get_computer_input() else -1

            if self.board.is_full():
                return 0

            if computer:
                best_value = -(sys.maxsize - 1)
                valid_moves = self.board.get_valid_moves()
                for move in valid_moves:
                    self.board.move(move, get_computer_input())
                    value = __min_max_solver(not computer, depth + 1)
                    self.board.undo_move()
                    if depth == 0 and best_value < value:
                        self.best_move = move
                    best_value = max(best_value, value)
                return best_value

            else:
                best_value = sys.maxsize
                valid_moves = self.board.get_valid_moves()
                for move in valid_moves:
                    self.board.move(move, get_user_input())
                    value = __min_max_solver(not computer, depth + 1)
                    self.board.undo_move()
                    best_value = min(best_value, value)
                return best_value

        return __min_max_solver(True, 0)
