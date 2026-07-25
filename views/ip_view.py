import customtkinter as ctk


class IpView(ctk.CTkFrame):
    def __init__(self, parent, controller, show_message):
        super().__init__(parent)
        
        self.controller = controller
        
        title = ctk.CTkLabel(
            self,
            text="Direcciones IP",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(20, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Crear y eliminar direcciones IP del router"
        )
        subtitle.pack(pady=(0, 20))

        form = ctk.CTkFrame(self)
        form.pack(padx=20, pady=10, fill="x")

        ctk.CTkLabel(form, text="Dirección IP").grid(
            row=0, column=0, padx=10, pady=(15, 5), sticky="w"
        )

        self.ip_entry = ctk.CTkEntry(
            form,
            placeholder_text="192.168.1.1/24",
            width=220
        )
        self.ip_entry.grid(row=1, column=0, padx=10, pady=(0, 15))

        ctk.CTkLabel(form, text="Interfaz").grid(
            row=0, column=1, padx=10, pady=(15, 5), sticky="w"
        )
        
        
        success, interfaces_values = self.controller.get_all_interfaces()
        
        if(not success):
            print(interfaces_values)
            interfaces_values = []

        self.interface_combo = ctk.CTkComboBox(
            form,
            values=interfaces_values
        )
        
        self.interface_combo.grid(row=1, column=1, padx=10)

        self.add_button = ctk.CTkButton(
            form,
            text="Agregar IP"
        )
        self.add_button.grid(
            row=1,
            column=2,
            padx=15
        )


        list_frame = ctk.CTkFrame(self)
        list_frame.pack(
            padx=20,
            pady=20,
            fill="both",
            expand=True
        )

        header = ctk.CTkFrame(list_frame, fg_color="transparent")
        header.pack(fill="x", padx=10, pady=(10, 5))

        ctk.CTkLabel(header, text="Dirección", width=180).grid(row=0, column=0)
        ctk.CTkLabel(header, text="Interfaz", width=120).grid(row=0, column=1)
        ctk.CTkLabel(header, text="Acción", width=100).grid(row=0, column=2)

        data = [
            ("192.168.1.1/24", "ether1"),
            ("10.10.10.1/24", "bridge"),
            ("172.16.0.1/16", "ether2")
        ]

        for ip, interface in data:

            row = ctk.CTkFrame(list_frame)
            row.pack(fill="x", padx=10, pady=4)

            ctk.CTkLabel(
                row,
                text=ip,
                width=180,
                anchor="w"
            ).grid(row=0, column=0, padx=5, pady=8)

            ctk.CTkLabel(
                row,
                text=interface,
                width=120
            ).grid(row=0, column=1)

            ctk.CTkButton(
                row,
                text="Eliminar",
                width=90
            ).grid(row=0, column=2, padx=5)