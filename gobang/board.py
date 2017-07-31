import itertools

EMPTY = -1
BLACK = 0
WHITE = 1

BOARD_SIZE = 15
FIVE = 5


class Game(object):

    def __init__(self):
        self.board = [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    def place(self, color, row, col):
        assert self.board[row][col] == EMPTY
        self.board[row][col] = color

    def is_win(self, row, col):
        """
        Check whether a player is win after placing a stone on (row, col)
        :param int row: 
        :param int col: 
        :rtype: bool 
        """
        board = self.board
        color = board[row][col]

        # horizontal
        n = 1
        for c in range(col-1, max(col-FIVE, 0), -1):
            if board[row][c] != color:
                break
            n += 1
        for c in range(col+1, min(col+FIVE, BOARD_SIZE)):
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
        for r in range(row+1, min(row+FIVE, BOARD_SIZE)):
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
        while r < BOARD_SIZE and c < BOARD_SIZE and board[r][c] == color:
            n += 1
            r += 1
            c += 1

        if n >= FIVE:
            return True

        # anti diagonal
        n = 1
        r, c = row-1, col+1
        while r >= 0 and c < BOARD_SIZE and board[r][c] == color:
            n += 1
            r -= 1
            c += 1

        r, c = row+1, col-1
        while r < BOARD_SIZE and c >= 0 and board[r][c] == color:
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
