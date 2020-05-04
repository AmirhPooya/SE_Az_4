from tkinter import *
from logic.game import Game
import user_interface.main_menu as m_m


def high_start(top):
    scores = Game.read_high_score()

    for widget in top.winfo_children():
        widget.destroy()

    button = Button(top, text="back", command=m_m.MainMenu.start)

    for i in range(len(scores)):
        label = Label(top, text=str(scores[i]))
        label.grid(row=i+1)

    button.grid(row=i+2)
