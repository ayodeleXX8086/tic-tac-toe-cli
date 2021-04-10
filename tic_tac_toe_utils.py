from copy import deepcopy
from typing import List, Tuple


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def board_draw(system_io):
    def draw(board):
        board_border = "".join(["*" for _ in range(len(board[0]) * 2)])
        system_io(board_border)
        for y in range(len(board)):
            line = "|"
            for x in range(len(board[0])):
                line += ((board[y][x] if board[y][x] else " ") + "|")
            system_io(line)
        system_io(board_border)

    return draw


def move_cursor(board, position, cursor_highlight):
    '''
    :param board: Current board state
    :param position: the position we want to move the cursor to on the board.
    :return The function would create a new board and return the new board with the highlighted cursor.
    The cursor would be rendered using the coursor highlighter.
    '''
    copy_board = deepcopy(board)
    copy_board[position[0]][
        position[1]] = f"{cursor_highlight}{copy_board[position[0]][position[1]] or '_'}{bcolors.ENDC}"
    return copy_board


def validate_move(board, movement, position):
    """
    :param board: This is games board
    :param movement: this is the game movement
    :param position: The current position
    :return: If this movement is a valid move
    """
    move_dictionary = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    if not movement in move_dictionary:
        return False, position
    moves = move_dictionary[movement]
    x, y = position[0] + moves[0], position[1] + moves[1]
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
        return False, position
    return True, (x, y)


def add_tic_or_toe_to_board(board: List[List], tic_or_toe: str, position: Tuple):
    board = deepcopy(board)
    if tic_or_toe.lower() != "x":
        return board
    if not board[position[0]][position[1]]:
        board[position[0]][position[1]] = tic_or_toe.upper()
    return board


def check_winner(board):
    '''

    :param board: The board is expected to be N by N
    :return: Tuple[bool, Optional[str]]
    '''
    # Check the board horizontal first
    for board_idx in range(len(board)):
        j = 0
        winner = True
        while j + 1 < len(board[0]) and winner:
            winner = winner and (board[board_idx][j] == board[board_idx][j + 1])
            j += 1
        if winner:
            return winner, board[board_idx][0]
    # check the board vertically.
    for board_idx in range(len(board[0])):
        i = 0
        winner = True
        while i + 1 < len(board) and winner:
            winner = winner and (board[i][board_idx] == board[i + 1][board_idx])
            i += 1
        if winner:
            return winner, board[0][board_idx]

    # Check diagonally to see if the tics could be crossed
    left_axis_winner = True
    right_axis_winner = True
    right_idx = len(board) - 1
    for board_idx in range(len(board) - 1):
        left_axis_winner = (left_axis_winner and board[board_idx][board_idx] == board[board_idx + 1][board_idx + 1])
        right_axis_winner = (right_axis_winner and board[board_idx][right_idx - board_idx] == board[board_idx + 1][
            right_idx - (board_idx + 1)])
    if left_axis_winner:
        return left_axis_winner, board[0][0]
    if right_axis_winner:
        return right_axis_winner, board[0][len(board) - 1]
    return False, None


def check_if_board_is_full(board):
    return all([all(b) for b in board])