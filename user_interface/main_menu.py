from tkinter import *
import user_interface.high_menu
from user_interface.game_menu import game_start


class MainMenu:
    @staticmethod
    def start(top=Tk()):
        for widget in top.winfo_children():
            widget.destroy()
        top.title("Quarto")
        game_button = Button(top, text="Start", command=lambda: game_start(top))
        game_button.pack()

        high_button = Button(top, text="High score", command=lambda: user_interface.high_menu.high_start(top))
        high_button.pack()

        exit_button = Button(top, text="Exit", command=exit)
        exit_button.pack()

        top.mainloop()

MainMenu.start()
