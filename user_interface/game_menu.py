from tkinter import *


def game_start(top):
    global current_piece
    for widget in top.winfo_children():
        widget.destroy()

    pieces = ["XX", "XO", "Xx", "Xo", "xX", "xO", "xx", "xo",
              "OX", "OO", "Ox", "Oo", "oX", "oO", "ox", "oo"]

    piece_buttons = []
    current_piece = None

    for i in range(len(pieces)):
        piece = pieces[i]
        piece_button = Button(top, text=piece, command=lambda: set_piece(piece))
        piece_buttons += [piece_button]
        piece_button.grid(row=0, column=i)


def set_piece(piece):
    global current_piece
    current_piece = piece
