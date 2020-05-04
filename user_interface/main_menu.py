from tkinter import *
from user_interface.high_menu import HighMenu
from user_interface.game_menu import game_start


class MainMenu:
    @staticmethod
    def start(top=Tk()):
        top.title("Quarto")
        game_button = Button(top, text="Start", command=lambda: game_start(top))
        game_button.pack()

        high_button = Button(top, text="High scores", command=lambda: HighMenu.start(top))
        high_button.pack()

        exit_button = Button(top, text="Exit", command=exit)
        exit_button.pack()

        top.mainloop()


MainMenu.start()
