from tkinter import *
from logic.game import Game


game = None
name_label = None


def game_start(top):
    global game, name_label, window
    window = top
    for widget in top.winfo_children():
        widget.destroy()

    game = Game(["AHP", "PKMS"])

    pieces = list(game.get_usable_piece_codes())

    piece_buttons = []

    for i in range(len(pieces)):
        piece = pieces[i]
        piece_button = Button(top, text=piece, command=lambda i=i: set_piece(pieces[i], piece_buttons[i]))
        piece_buttons += [piece_button]
        piece_button.grid(row=0, column=i)

    grid = game.cells
    grid_buttons = []

    for i in range(4):
        button_row = []
        for j in range(4):
            cell = grid[i][j]
            cell_text = '‌ ‌ ‌ ‌‌‌‌'
            if cell is not None:
                cell_text = cell.code
            grid_button = Button(top, text=cell_text, command=lambda i=i, j=j: put_piece(i, j, grid_buttons[i][j]))
            grid_button.grid(row=i+3, column=j+6)
            button_row += [grid_button]
        grid_buttons += [button_row]
    name = game.current_name()
    name_label = Label(top, text=name)
    name_label.grid(row=1, column=5)


def set_piece(piece, button):
    if game.choose_piece(piece):
        button.config(text='‌ ‌ ‌ ‌‌‌‌')
    name = game.current_name()
    name_label.config(text=name)


def put_piece(i, j, button):
    global window
    piece = game.place_piece(i, j)
    if piece == 1:
        name_label.config(text=game.current_name() + " WON!")
        game.save_high_score()
        window.quit()
        return
    if piece is not None:
        button.config(text=piece)



