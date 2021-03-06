from gobang.const import NONE, BOARD_HEIGHT, Color, BOARD_WIDTH, FIVE, BLACK, WHITE


def opponent_of(color: Color) -> Color:
    assert color != NONE
    return WHITE if color == BLACK else BLACK


class Game:
    def __init__(self):
        self._board = []
        """:type: List[List[Color]]"""

        # todo is there an official name?
        self._history = []
        self._resigned = NONE
        self._winner = NONE
        self._finished = False

    def start(self):
        self._board = [[NONE] * BOARD_HEIGHT for _ in range(BOARD_WIDTH)]
        self._history = []
        self._resigned = self._winner = NONE
        self._finished = False

    def make_move(self, color: Color, row: int, col: int):
        # assert self._board[row][col] == NONE
        self._board[row][col] = color
        self._history.append((row, col))
        self._check_finished()

    def resign(self, color: Color):
        self._resigned = color
        self._winner = opponent_of(color)
        self._finished = True

    def last_moved_color(self) -> Color:
        if not self._history:
            return NONE

        return BLACK if len(self._history) % 2 == 1 else WHITE

    def get_winner(self) -> Color:
        return self._winner

    def is_finished(self) -> bool:
        return self._finished

    def _check_finished(self):
        """        
        Checks whether the last move ends the game. 
        """
        # todo support Renju rules.

        if self._resigned != NONE:
            return True

        if not self._history:
            return False

        board = self._board
        row, col = self._history[-1]
        color = board[row][col]

        # horizontal
        n = 1
        for c in range(col-1, max(col-FIVE, 0), -1):
            if board[row][c] != color:
                break
            n += 1
        for c in range(col+1, min(col+FIVE, BOARD_WIDTH)):
            if board[row][c] != color:
                break
            n += 1

        if n >= FIVE:
            return True

        # vertical
        n = 1
        for r in range(row-1, max(row-FIVE, 0), -1):
            if board[r][col] != color:
                break
            n += 1
        for r in range(row+1, min(row+FIVE, BOARD_HEIGHT)):
            if board[r][col] != color:
                break
        if n >= FIVE:
            return True

        # main diagonal
        n = 1
        r, c = row-1, col-1
        while r >= 0 and c >= 0 and board[r][c] == color:
            n += 1
            r -= 1
            c -= 1

        r, c = row+1, col+1
        while r < BOARD_HEIGHT and c < BOARD_WIDTH and board[r][c] == color:
            n += 1
            r += 1
            c += 1

        if n >= FIVE:
            return True

        # anti diagonal
        n = 1
        r, c = row-1, col+1
        while r >= 0 and c < BOARD_WIDTH and board[r][c] == color:
            n += 1
            r -= 1
            c += 1

        r, c = row+1, col-1
        while r < BOARD_HEIGHT and c >= 0 and board[r][c] == color:
            n += 1
            r += 1
            c -= 1

        if n >= FIVE:
            return True

        return False

#
# def iterate_rows():
#     def row_iterator(row_):
#         for col in range(BOARD_SIZE):
#             yield row_, col
#
#     for row in range(BOARD_SIZE):
#         yield row_iterator(row)
#
#
# def iterate_cols():
#     def col_iterator(col_):
#         for row in range(BOARD_SIZE):
#             yield row, col_
#
#     for col in range(BOARD_SIZE):
#         yield col_iterator(col)
#
#
# # todo how to name the two diagonals?
# def iterate_main_diagonal():
#
#
# def iterate_lines():
#     return itertools.chain(iterate_rows(), iterate_cols())
#
#
# if __name__ == '__main__':
#     for line in iterate_lines():
#         for r, c in line:
#             print(r, c)
