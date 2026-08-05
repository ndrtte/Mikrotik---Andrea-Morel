import customtkinter as ctk

class IpView(ctk.CTkFrame):
    
    """
        Vista para crear y eliminar las IPS y verlas tambien
    """
    def __init__(self, parent, controller, show_message, interface_util):
        super().__init__(parent, fg_color="transparent")

        self.controller = controller
        self.show_message = show_message
        self.interface_util = interface_util
        self.interface_combo = None

        title = ctk.CTkLabel(
            self,
            text="Direcciones IP",
            font=ctk.CTkFont(family="Poppins", size=20, weight="bold"),
            text_color="#C2185B"
        )
        title.pack(pady=(10, 5), anchor="w", padx=20)

        subtitle = ctk.CTkLabel(
            self,
            text="Crear y eliminar direcciones IP del router",
            font=ctk.CTkFont(family="Poppins", size=12),
            text_color="#6A1B9A"
        )
        subtitle.pack(pady=(0, 20), anchor="w", padx=20)

        form = ctk.CTkFrame(
            self, corner_radius=16,
            fg_color="#FDF2F8", border_width=1, border_color="#F8BBD0"
        )
        form.pack(padx=20, pady=10, fill="x")

        ctk.CTkLabel(
            form, text="Dirección IP",
            font=ctk.CTkFont(family="Poppins", size=12),
            text_color="#AD1457"
        ).grid(row=0, column=0, padx=10, pady=(15, 5), sticky="w")

        self.ip_entry = ctk.CTkEntry(
            form,
            placeholder_text="192.168.1.1/24",
            font=ctk.CTkFont(family="Poppins", size=13),
            width=220
        )
        self.ip_entry.grid(row=1, column=0, padx=10, pady=(0, 15))

        ctk.CTkLabel(
            form, text="Interfaz",
            font=ctk.CTkFont(family="Poppins", size=12),
            text_color="#AD1457"
        ).grid(row=0, column=1, padx=10, pady=(15, 5), sticky="w")

        success, interfaces_values = self.interface_util.get_all_interfaces()

        if success:
            self.interface_combo = ctk.CTkComboBox(
                form,
                values=interfaces_values,
                font=ctk.CTkFont(family="Poppins", size=13)
            )
        else:
            self.interface_combo = ctk.CTkComboBox(
                form,
                values=[],
                font=ctk.CTkFont(family="Poppins", size=13)
            )
            self.show_message(f"Error cargando interfaces: {interfaces_values}")

        self.interface_combo.grid(row=1, column=1, padx=10, pady=(0, 15))

        self.add_button = ctk.CTkButton(
            form,
            text="Agregar IP",
            fg_color="#EC407A", hover_color="#C2185B",
            font=ctk.CTkFont(family="Poppins", size=13, weight="bold"),
            command=lambda: self.create_ip(self.ip_entry.get(), self.interface_combo.get())
        )
        self.add_button.grid(row=1, column=2, padx=15, pady=(0, 15))

        self.list_frame = ctk.CTkScrollableFrame(
            self, fg_color="#FDF2F8", corner_radius=16
        )
        self.list_frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.create_table_header()
        self.load_ips()

    def create_table_header(self):
        header = ctk.CTkFrame(self.list_frame, fg_color="transparent")
        header.pack(fill="x", padx=10, pady=(10, 5))

        header_font = ctk.CTkFont(family="Poppins", size=12, weight="bold")

        ctk.CTkLabel(header, text="Dirección", width=180, font=header_font, text_color="#880E4F").grid(row=0, column=0)
        ctk.CTkLabel(header, text="Red", width=140, font=header_font, text_color="#880E4F").grid(row=0, column=1)
        ctk.CTkLabel(header, text="Interfaz", width=120, font=header_font, text_color="#880E4F").grid(row=0, column=2)
        ctk.CTkLabel(header, text="Acción", width=90, font=header_font, text_color="#880E4F").grid(row=0, column=3)

    #Aca de cargan en las tablas
    def load_ips(self):
        for widget in self.list_frame.winfo_children():
            if widget.winfo_name() != "!ctkframe":
                widget.destroy()

        success, ip_values = self.controller.get_all_ip()

        if not success:
            self.show_message(f"Error cargando IPs: {ip_values}")
            return

        for item in ip_values:

            row = ctk.CTkFrame(self.list_frame, fg_color="#FFFFFF", corner_radius=10)
            row.pack(fill="x", padx=10, pady=4)

            row_font = ctk.CTkFont(family="Poppins", size=13)

            ctk.CTkLabel(
                row, text=item["ip"], width=180, anchor="w",
                font=row_font, text_color="#880E4F"
            ).grid(row=0, column=0, padx=5, pady=8)

            ctk.CTkLabel(
                row, text=item["network"], width=140,
                font=row_font, text_color="#6A1B9A"
            ).grid(row=0, column=1, padx=5)

            ctk.CTkLabel(
                row, text=item["interface"], width=120,
                font=row_font, text_color="#6A1B9A"
            ).grid(row=0, column=2, padx=5)

            ctk.CTkButton(
                row,
                text="Eliminar",
                width=90,
                fg_color="#C62828", hover_color="#8E0000",
                font=ctk.CTkFont(family="Poppins", size=12),
                command=lambda ip=item["ip"]: self.delete_ip(ip)
            ).grid(row=0, column=3, padx=5)

    #Para crearlas solo se manda parametro de ip e interfaz
    def create_ip(self, ip, interface):
        success, message = self.controller.create_ip(ip, interface)
        self.show_message(message)

        if success:
            self.ip_entry.delete(0, "end")
            #Para volver a cargar 
            self.load_ips()

    #Eliminar solo por ip para comparar en el controlador
    def delete_ip(self, ip):
        success, message = self.controller.delete_ip(ip)
        self.show_message(message)

        if success:
            self.load_ips()