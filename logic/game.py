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
