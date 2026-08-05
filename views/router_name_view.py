import customtkinter as ctk

class RouterNameView(ctk.CTkFrame):
    """
        Vista para asignar nombre al router
    """
    def __init__(self, parent, controller, show_message):
            super().__init__(parent, fg_color="transparent")
            self.controller = controller
            self.app = parent.master
            self.show_message = show_message

            self.title = ctk.CTkLabel(
                self,
                text="Asignar nombre al Router",
                font=ctk.CTkFont(family="Poppins", size=20, weight="bold"),
                text_color="#C2185B"
            )
            self.title.pack(pady=(10, 20), anchor="w", padx=20)

            self.card = ctk.CTkFrame(
                self, corner_radius=16,
                fg_color="#FDF2F8", border_width=1, border_color="#F8BBD0"
            )
            self.card.pack(fill="x", padx=20)

            self.subtitle = ctk.CTkLabel(
                self.card,
                text="Nombre actual",
                font=ctk.CTkFont(family="Poppins", size=13),
                text_color="#AD1457"
            )
            self.subtitle.pack(pady=(15, 0), padx=15, anchor="w")

            self.router_name = ctk.CTkLabel(
                self.card,
                text="--", #Por defecto es este el nombre
                font=ctk.CTkFont(family="Poppins", size=16, weight="bold"),
                text_color="#880E4F"
            )
            self.router_name.pack(pady=(0, 15), padx=15, anchor="w")

            self.load_router_name() #Para cargar el nombre del controlador

            self.description = ctk.CTkLabel(
                self.card,
                text="Ingrese el nuevo nombre del dispositivo",
                font=ctk.CTkFont(family="Poppins", size=12),
                text_color="#6A1B9A"
            )
            self.description.pack(padx=15, anchor="w")

            self.router_name_entry = ctk.CTkEntry(
                self.card,
                placeholder_text="Ejemplo: Router-Principal",
                font=ctk.CTkFont(family="Poppins", size=13)
            )
            self.router_name_entry.pack(fill="x", padx=15, pady=(5, 10))

            self.save_button = ctk.CTkButton(
                self.card,
                text="Guardar nombre",
                fg_color="#EC407A", hover_color="#C2185B",
                font=ctk.CTkFont(family="Poppins", size=13, weight="bold"),
                command=self.save_new_router_name
            )
            self.save_button.pack(padx=15, pady=(0, 15), anchor="w")

            self.status_label = ctk.CTkLabel(
                self,
                text="",
                font=ctk.CTkFont(family="Poppins", size=12)
            )
            self.status_label.pack(pady=10)

    def load_router_name(self):
        router_name = self.controller.get_router_identity() 
        self.router_name.configure(text=router_name) #Esta funcion lo que hace es acceder al valor del Label

    def save_new_router_name(self):
        new_name = self.router_name_entry.get()
        success, message = self.controller.update_router_name(new_name) #Para guardar el nuevo nombre
        self.show_message(message)

        if success:
            self.router_name_entry.delete(0, "end")
            self.load_router_name()