import customtkinter as ctk

class IpView(ctk.CTkFrame):
    def __init__(self, parent, controller, show_message, interface_util):
        super().__init__(parent)
        
        self.controller = controller
        self.show_message = show_message
        self.interface_util = interface_util
        
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
        
        
        success, interfaces_values = self.interface_util.get_all_interfaces()

        if success:
            self.interface_combo = ctk.CTkComboBox(
                form,
                values=interfaces_values
            )

            self.interface_combo.grid(
                row=1,
                column=1,
                padx=10
            )

        else:
            self.show_message(
                f"Error cargando interfaces: {interfaces_values}"
            )
        
        self.interface_combo.grid(row=1, column=1, padx=10)

        self.add_button = ctk.CTkButton(
            form,
            text="Agregar IP",
            command= lambda: self.create_ip( self.ip_entry.get(),self.interface_combo.get())
        )
        self.add_button.grid(
            row=1,
            column=2,
            padx=15
        )


        self.list_frame = ctk.CTkFrame(self)
        self.list_frame.pack(
            padx=20,
            pady=20,
            fill="both",
            expand=True
        )

        self.create_table_header()

        self.load_ips()
    
    def create_table_header(self):
        header = ctk.CTkFrame(self.list_frame, fg_color="transparent")
        header.pack(fill="x", padx=10, pady=(10, 5))

        ctk.CTkLabel(header, text="Dirección", width=180).grid(row=0, column=0)
        ctk.CTkLabel(header, text="Red", width=140).grid(row=0, column=1)
        ctk.CTkLabel(header, text="Interfaz", width=120).grid(row=0, column=2)
        ctk.CTkLabel(header, text="Acción", width=90).grid(row=0, column=3)
        
    def load_ips(self):
        for widget in self.list_frame.winfo_children():
            if widget.winfo_name() != "!ctkframe": 
                widget.destroy()

        success, ip_values = self.controller.get_all_ip()

        if not success:
            self.show_message(f"Error cargando IPs: {ip_values}")
            return

        for item in ip_values:

            row = ctk.CTkFrame(self.list_frame)
            row.pack(fill="x", padx=10, pady=4)

            ctk.CTkLabel(
                row,
                text=item["ip"],
                width=180,
                anchor="w"
            ).grid(row=0, column=0, padx=5, pady=8)

            ctk.CTkLabel(
                row,
                text=item["network"],
                width=140
            ).grid(row=0, column=1, padx=5)

            ctk.CTkLabel(
                row,
                text=item["interface"],
                width=120
            ).grid(row=0, column=2, padx=5)

            ctk.CTkButton(
                row,
                text="Eliminar",
                width=90,
                command=lambda ip=item["ip"]: self.delete_ip(ip)
            ).grid(row=0, column=3, padx=5)
    
    def create_ip(self, ip, interface):
        success, message = self.controller.create_ip(ip, interface)
        self.show_message(message)

        if success:
            self.load_ips()
    
    def delete_ip(self, ip):
        success, message = self.controller.delete_ip(ip)
        self.show_message(message)

        if success:
            self.load_ips()