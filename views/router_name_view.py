import customtkinter as ctk 

import customtkinter as ctk


class RouterNameView(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        print("Se muestra en pantalla")

        self.title = ctk.CTkLabel(
            self,
            text="Asignar nombre al Router",
            font = ctk.CTkFont(size=22, weight="bold")
        )
        self.title.pack(pady=20)
        
        self.subtitle = ctk.CTkLabel(
            self,
            text="Nombre del Router",
            font= ctk.CTkFont(size=16, weight="bold")
        )
        
        self.subtitle.pack(pady=5)
        
        self.router_name = ctk.CTkLabel(
            self,
            text="R1",
            font= ctk.CTkFont(size=14)
        )

        self.router_name.pack()

        self.description = ctk.CTkLabel(
            self,
            text="Ingrese el nuevo nombre del dispositivo"
        )
        self.description.pack(pady=5)


        self.router_name_entry = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Ejemplo: Router-Principal"
        )
        self.router_name_entry.pack(pady=10)

        self.save_button = ctk.CTkButton(
            self,
            text="Guardar nombre"
        )
        self.save_button.pack(pady=20)

        self.status_label = ctk.CTkLabel(
            self,
            text=""
        )
        self.status_label.pack()

        
        
        