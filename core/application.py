import customtkinter as ctk
from config import APP_NAME, WINDOW_HEIGHT, WINDOW_WIDTH

class Application(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title(APP_NAME)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
