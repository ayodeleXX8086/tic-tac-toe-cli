from cli_utils import *
from game_handler import GameBoard, MOVE_DICTIONARY, get_computer_input, get_user_input
from min_max_algo import MinMaxAlgorithm


def generate_board():
    return [["" for _ in range(3)] for _ in range(3)], (0, 0)


def calculate_new_position(key, curr_position):
    move = MOVE_DICTIONARY[key]
    return [curr_position[0] + move[0], curr_position[1] + move[1]]


def end_game(board):
    if board.game_is_over():
        is_winning, winner = board.check_winner()
        board.draw_tic_tac()
        if is_winning:
            print(f"The winner of this game is {winner}")
        else:
            print("This is a draw")
        return True
    return False


def play_game():
    """
    Game Controller
    """
    board = GameBoard()
    min_max = MinMaxAlgorithm(board)
    curr_position = [0, 0]
    while True:
        board.move_cursor(curr_position)
        clear_screen()
        board.draw_tic_tac()
        key = get_input()
        if key == "exit":
            break
        if key in MOVE_DICTIONARY:
            new_curr_position = calculate_new_position(key, curr_position)
            if board.validate_position(new_curr_position):
                curr_position = new_curr_position
                board.move_cursor(curr_position)
            continue

        if get_user_input().lower() == key.lower() and board.is_valid_move(curr_position, get_user_input()):
            board.move(curr_position, get_user_input())
        else:
            continue

        if end_game(board):
            break
        min_max.min_max_solver()
        board.move(min_max.best_move, get_computer_input())

        if end_game(board):
            break


if __name__ == "__main__":
    prepare_terminal()
    play_game()
