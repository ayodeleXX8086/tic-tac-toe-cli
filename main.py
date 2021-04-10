from cli_utils import *
from tic_tac_toe_utils import board_draw, move_cursor, bcolors, validate_move, add_tic_or_toe_to_board


def generate_board():
    return [["" for _ in range(3)] for _ in range(3)], (0, 0)


def play_game():
    """
    Game Controller WIP
    :TODO Convert these flows into a chain method.
    """
    board, position = generate_board()
    draw = board_draw(print)
    while True:
        draw_board = move_cursor(board, position, bcolors.OKBLUE)
        clear_screen()
        draw(draw_board)
        key = get_input()
        if key == "exit":
            break
        _, position = validate_move(board, key, position)
        board = add_tic_or_toe_to_board(board, key, position)


if __name__ == "__main__":
    prepare_terminal()
    play_game()
