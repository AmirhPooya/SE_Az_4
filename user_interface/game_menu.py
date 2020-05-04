from tkinter import *
from logic.game import Game


game = None

def update_turn(name):
    pass

def game_start(top):
    global game
    for widget in top.winfo_children():
        widget.destroy()

    game = Game(["Poosa", "Ostad"])

    pieces = ["XX", "XO", "Xx", "Xo", "xX", "xO", "xx", "xo",
              "OX", "OO", "Ox", "Oo", "oX", "oO", "ox", "oo"]

    piece_buttons = []

    for i in range(len(pieces)):
        piece = pieces[i]
        piece_button = Button(top, text=piece, command=lambda i=i: set_piece(pieces[i]))
        piece_buttons += [piece_button]
        piece_button.grid(row=0, column=i)

    grid = game.cells
    for i in range(4):
        for j in range(4):
            cell = grid[i][j]
            cell_text = '  '
            if cell is not None:
                cell_text = cell.code
            grid_button = Button(top, text=cell_text, command=lambda i=i, j=j: put_piece(i, j))
            grid_button.grid(row=i+3, column=j+6)


def set_piece(piece):
    game.choose_piece(piece)


def put_piece(i, j):
    game.place_piece(i, j)
    name = game.current_name()
