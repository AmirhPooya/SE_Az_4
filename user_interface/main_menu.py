from tkinter import *
from user_interface.high_menu import HighMenu
from user_interface.game_menu import GameMenu


class MainMenu:
    @staticmethod
    def start(top=Tk()):
        top.title("Quarto")
        top.geometry('230x100')
        game_button = Button(top, text="Start", command=GameMenu.start)
        game_button.pack()

        high_button = Button(top, text="High scores", command=HighMenu.start)
        high_button.pack()

        exit_button = Button(top, text="Exit", command=exit)
        exit_button.pack()

        top.mainloop()


MainMenu.start()
