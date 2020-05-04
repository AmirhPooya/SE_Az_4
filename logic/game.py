import random

from logic import Piece


class Game:
    def __init__(self):
        self.cells = [[None for _ in range(4)] for _ in range(4)]
        self.placed_pieces = set()
        self.usable_pieces = set()
        self.turn = random.randint(1, 2)
        self.chosen_piece = None
        self.turns_count = 0

        try:
            with open('highscore.txt', 'r') as f:
                self.high_score = int(f.read())
        except FileNotFoundError:
            self.high_score = None

        for height in ['tall', 'short']:
            for color in ['black', 'white']:
                for shape in ['square', 'circle']:
                    for hollow_top in [True, False]:
                        self.usable_pieces.add(Piece(height, color, shape, hollow_top))

    def get_usable_piece_codes(self):
        return {
            piece.code for piece in self.usable_pieces
        }

    def get_piece(self, code):
        for piece in self.usable_pieces:
            if piece.code == code:
                return piece

    def choose_piece(self, code):
        piece = self.get_piece(code)
        if self.chosen_piece is not None or piece is None:
            return
        self.chosen_piece = piece

    @staticmethod
    def check_win(pieces):
        try:
            if (
                    pieces[0].height == pieces[1].height == pieces[2].height == pieces[3].height or
                    pieces[0].color == pieces[1].color == pieces[2].color == pieces[3].color or
                    pieces[0].shape == pieces[1].shape == pieces[2].shape == pieces[3].shape or
                    pieces[0].hollow_top == pieces[1].hollow_top == pieces[2].hollow_top == pieces[3].hollow_top
            ):
                return True
        except AttributeError:
            return False
        return False

    def save_high_score(self):
        if self.high_score is not None and self.turns_count >= self.high_score:
            return
        with open('highscore.txt', 'w') as f:
            f.write(str(self.turns_count))

    def place_piece(self, row, column):
        if self.chosen_piece is None or self.cells[row][column] is not None:
            return -2
        self.turns_count += 1
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
