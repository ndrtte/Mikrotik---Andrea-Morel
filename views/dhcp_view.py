import customtkinter as ctk


class DhcpView(ctk.CTkFrame):
    def __init__(self, parent, controller, show_message):
        super().__init__(parent)

        self.controller = controller
        self.show_message = show_message

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.title = ctk.CTkLabel(
            self,
            text="Administración de DHCP",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title.grid(row=0, column=0, pady=(20, 5))

        self.subtitle = ctk.CTkLabel(
            self,
            text="Visualiza, crea y elimina servidores DHCP.",
            text_color="gray"
        )
        self.subtitle.grid(row=1, column=0, pady=(0, 15))

        self.table = ctk.CTkFrame(self)
        self.table.grid(row=2, column=0, padx=20, sticky="nsew")

        headers = [
            "Nombre",
            "Interfaz",
            "Pool",
            "Gateway",
            "Estado"
        ]

        for col, text in enumerate(headers):
            lbl = ctk.CTkLabel(
                self.table,
                text=text,
                font=ctk.CTkFont(weight="bold")
            )
            lbl.grid(row=0, column=col, padx=10, pady=10)


        fake_data = [
            ("DHCP-LAN", "ether2", "Pool-LAN", "192.168.1.1", "Activo"),
            ("DHCP-WIFI", "wlan1", "Pool-WIFI", "192.168.10.1", "Activo"),
            ("Invitados", "bridge", "Pool-Guest", "10.10.10.1", "Deshabilitado")
        ]

        self.selected = ctk.StringVar(value="")

        for row, item in enumerate(fake_data, start=1):
            radio = ctk.CTkRadioButton(
                self.table,
                text=item[0],
                variable=self.selected,
                value=item[0]
            )
            radio.grid(row=row, column=0, padx=10, pady=8, sticky="w")

            ctk.CTkLabel(self.table, text=item[1]).grid(row=row, column=1, padx=10)
            ctk.CTkLabel(self.table, text=item[2]).grid(row=row, column=2, padx=10)
            ctk.CTkLabel(self.table, text=item[3]).grid(row=row, column=3, padx=10)
            ctk.CTkLabel(self.table, text=item[4]).grid(row=row, column=4, padx=10)

        self.buttons = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons.grid(row=3, column=0, pady=20)

        self.create_btn = ctk.CTkButton(
            self.buttons,
            text="Crear DHCP",
            width=150
        )
        self.create_btn.grid(row=0, column=0, padx=10)

        self.delete_btn = ctk.CTkButton(
            self.buttons,
            text="Eliminar DHCP",
            width=150
        )
        self.delete_btn.grid(row=0, column=1, padx=10)