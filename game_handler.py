MOVE_DICTIONARY = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


def get_computer_input():
    return "X"


def get_user_input():
    return "O"


EMPTY = None


def generate_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]


class GameBoard:
    def __init__(self):
        self.board = generate_board()
        self.curr_player = get_user_input()
        self.moves = []
        self.cursor_position = [0, 0]

    def move_cursor(self, position: list[int, int]):
        self.cursor_position = position

    def get_valid_moves(self):
        result = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == EMPTY:
                    result.append((i, j))
        return result

    def move(self, position: list[int, int], tic_or_tac: str):
        if not self.is_valid_move(position, tic_or_tac):
            return False
        self.board[position[0]][position[1]] = tic_or_tac
        self.moves.append((position, tic_or_tac))
        self.curr_player = self.next_player()
        return False

    def undo_move(self):
        if not self.moves:
            return
        prev_pos, tic_or_tac = self.moves.pop()
        self.board[prev_pos[0]][prev_pos[1]] = EMPTY
        self.curr_player = tic_or_tac

    def add_tic_or_tac(self, tic_or_tac: str, position: list[int, int]):
        self.board[position[0]][position[1]] = tic_or_tac
        return

    def game_is_over(self):
        is_winner, _ = self.check_winner()
        is_full = self.is_full()
        return is_winner or is_full

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != EMPTY:
                return True, row[0]

        for col in range(len(self.board)):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != EMPTY:
                return True, self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != EMPTY:
            return True, self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != EMPTY:
            return True, self.board[0][2]

        return False, EMPTY

    def draw_tic_tac(self):
        board_border = "".join(["_" for _ in range(len(self.board[0]) * 2)])
        print(board_border)
        for y in range(len(self.board)):
            line = "|"
            for x in range(len(self.board[0])):
                if [y, x] == self.cursor_position:
                    cursor = ((self.board[y][x] if self.board[y][x] else "_") + "|")
                    line += f"{cursor}"
                else:
                    line += ((self.board[y][x] if self.board[y][x] else " ") + "|")
            print(line)
        print(board_border)

    def is_full(self):
        return all([all([c is not EMPTY for c in b]) for b in self.board])

    def is_valid_move(self, position, tic_or_tac):
        if tic_or_tac != self.curr_player:
            return False
        if not self.validate_position(position):
            return False
        return self.board[position[0]][position[1]] == EMPTY

    def next_player(self):
        return get_computer_input() if self.curr_player == get_user_input() else get_user_input()

    def validate_position(self, position: list[int, int]) -> bool:
        new_position_y, new_position_x = position
        if 0 <= new_position_y < len(self.board) and 0 <= new_position_x < len(self.board[0]):
            return True
        return False
