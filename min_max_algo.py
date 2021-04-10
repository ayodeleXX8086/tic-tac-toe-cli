import sys
from copy import deepcopy

from tic_tac_toe_utils import check_winner, check_if_board_is_full


def _get_valid_moves(board, computer):
    '''
    Based on the current state of the board, this function makes a valid move and
    returns the board with a move and the point of the move
    complexity O(N^M) N is the number of legal moves such as the Nodes of the graph and M is the depth of the Graph
    :param board: is a 2 dimensional board
    :param computer: Boolean variable that shows if it is a computer it set to True, if not is set to False
    :return: returns the board move and points
    '''
    cloned_board = deepcopy(board)
    for i in range(len(cloned_board)):
        for j in range(len(cloned_board[0])):
            if cloned_board[i][j] == ' ':
                cloned_board[i][j] = 'O' if computer else 'X'
                yield cloned_board, (i, j)


def __min_max_solver(board, depth, points, computer):
    '''
    To discover the best move by the computer it is ideal for the computer try all moves, this move is then traversed in a graph
    structure using a  DFS, for each move the computer will stimulates the user and computer playing different moves, it will then
    search for the path with the maximum possibility and the minimum possibilty of the user winning.
    For each node traversal there are three terminal states Such as (1) Computer winning, (-1) Computer lost, (0) A tie
    :param board: 2d array
    :param depth: depth how far as the board gone
    :param points: calculated points
    :param computer: player identity
    '''
    if check_winner(board):
        value = check_winner(board)[0]
        return 1 if value == 'O' else -1

    if check_if_board_is_full(board):
        return 0

    if computer:
        best_value = -(sys.maxsize - 1)
        for child in _get_valid_moves(board, computer):
            value = __min_max_solver(child[0], depth + 1, points, False)
            if depth == 0:
                points.append((child[1], value))
            child[0][child[1][0]][child[1][1]] = ' '
            best_value = max(best_value, value)
        return best_value

    else:
        best_value = sys.maxsize
        for child in _get_valid_moves(board, computer):
            value = __min_max_solver(child[0], depth + 1, points, True)
            child[0][child[1][0]][child[1][1]] = ' '
            best_value = min(best_value, value)
        return best_value
