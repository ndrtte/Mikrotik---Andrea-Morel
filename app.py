import customtkinter as ctk

from config import *
#from core.application import Application

ctk.set_appearance_mode(APPEARANCE)
ctk.set_default_color_theme(THEME)

app = Application()
app.mainloop()