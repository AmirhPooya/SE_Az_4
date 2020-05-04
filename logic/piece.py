class Piece:
    def __init__(self, height, color, shape, hollow_top):
        self.row = None
        self.column = None
        self.height = height
        self.color = color
        self.shape = shape
        self.hollow_top = hollow_top
        first_char = 'x' if color == 'black' else 'o'
        if height == 'tall':
            first_char = first_char.capitalize()
        second_char = 'x' if shape == 'square' else 'o'
        if hollow_top:
            second_char = second_char.capitalize()
        self.code = first_char + second_char
