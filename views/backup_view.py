import customtkinter as ctk

class BackupView(ctk.CTkFrame):
    def __init__(self, parent, controller, show_message):
            super().__init__(parent)
    
            self.controller = controller
            self.show_message = show_message