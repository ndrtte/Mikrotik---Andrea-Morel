import customtkinter as ctk


class Notification(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.label = ctk.CTkLabel(self,text="")

        self.label.pack(padx=20,pady=10)


    def show(self, message):
        self.label.configure(
            text=message
        )
        
        self.pack(
            side="bottom",
            fill="x"
        )


    def hide(self):
        self.pack_forget()