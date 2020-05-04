import random

from logic import Piece


class Game:
    def __init__(self):
        self.cells = [[None for _ in range(4)] for _ in range(4)]
        self.placed_pieces = set()
        self.usable_pieces = set()
        self.turn = random.randint(1, 2)
        self.chosen_piece = None
        self.piece_placed = False

        for height in ['tall', 'short']:
            for color in ['black', 'white']:
                for shape in ['square', 'circle']:
                    for hollow_top in [True, False]:
                        self.usable_pieces.add(Piece(height, color, shape, hollow_top))

    def choose_piece(self, piece):
        if self.chosen_piece is not None:
            return
        self.chosen_piece = piece

    @staticmethod
    def check_win(pieces):
        if (
                pieces[0].height == pieces[1].height == pieces[2].height == pieces[3].height or
                pieces[0].height == pieces[1].height == pieces[2].height == pieces[3].height
        ):
            return True
        return False

    def place_piece(self, row, column):
        if self.piece_placed or self.chosen_piece is None or self.cells[row][column] is not None:
            return -2
        self.placed_pieces.add(self.chosen_piece)
        self.usable_pieces.remove(self.chosen_piece)
        self.cells[row][column] = self.chosen_piece

        if (
            self.check_win(self.cells[row]) or
            self.check_win([self.cells[i][column] for i in range(4)]) or
            (row == column and self.check_win([self.cells[i][i] for i in range(4)]))
        ):
            return 1
        if len(self.placed_pieces) == 16:
            return -1
        return 0
