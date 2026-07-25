import customtkinter as ctk 

class RouterNameView(ctk.CTkFrame):
    def __init__(self, parent, controller, show_message):
            super().__init__(parent)
            self.controller = controller
            self.app = parent.master
            self.show_message = show_message

            print("Pantalla de nombre de router")

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
                text="",
                font=ctk.CTkFont(size=14)
            )

            self.router_name.pack()

            self.load_router_name()

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
                text="Guardar nombre",
                command=self.save_new_router_name
            )
            self.save_button.pack(pady=20)

            self.status_label = ctk.CTkLabel(
                self,
                text=""
            )
            self.status_label.pack()
    
    def load_router_name(self):
        router_name = self.controller.get_router_identity()
        self.router_name.configure(text=router_name)
    
    def save_new_router_name(self):
        new_name = self.router_name_entry.get()
        success, message = self.controller.update_router_name(new_name)
        self.show_message(message)

        if success:
            self.load_router_name()

        
        
        