import customtkinter as ctk

from config import APPEARANCE, THEME
from core.application import Application

ctk.set_appearance_mode(APPEARANCE)
ctk.set_default_color_theme(THEME)

if __name__ == "__main__":
    app = Application()
    app.mainloop()