import customtkinter as ctk


class DnsView(ctk.CTkFrame):
    def __init__(self, parent, controller, show_message):
        super().__init__(parent)

        self.controller = controller
        self.show_message = show_message

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.header_font = ctk.CTkFont(size=20, weight="bold")
        self.label_font = ctk.CTkFont(size=13)
        self.small_font = ctk.CTkFont(size=12)
        self.small_bold_font = ctk.CTkFont(size=12, weight="bold")

        self.build_left_column()
        self.build_right_column()

    def build_left_column(self):
        self.config_frame = ctk.CTkFrame(self, corner_radius=12)
        self.config_frame.grid(row=0, column=0, sticky="nsew", padx=(20, 10), pady=20)
        self.config_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self.config_frame, text="Configurar Servidores DNS", font=self.header_font
        ).grid(row=0, column=0, sticky="w", padx=20, pady=(20, 15))

        ctk.CTkLabel(self.config_frame, text="Servidores DNS", font=self.label_font).grid(
            row=1, column=0, sticky="w", padx=20
        )
        self.dns_servers_entry = ctk.CTkEntry(
            self.config_frame, placeholder_text="8.8.8.8,1.1.1.1"
        )
        self.dns_servers_entry.grid(row=2, column=0, sticky="ew", padx=20, pady=(2, 15))

        ctk.CTkLabel(
            self.config_frame, text="Allow Remote Requests", font=self.label_font
        ).grid(row=3, column=0, sticky="w", padx=20)
        self.remote_requests_combo = ctk.CTkComboBox(self.config_frame, values=["Sí", "No"])
        self.remote_requests_combo.grid(row=4, column=0, sticky="ew", padx=20, pady=(2, 25))

        self.save_dns_button = ctk.CTkButton(
            self.config_frame, text="Guardar Configuración DNS"
        )
        self.save_dns_button.grid(row=5, column=0, sticky="ew", padx=20, pady=(0, 20))

    def build_right_column(self):
        self.current_config_frame = ctk.CTkFrame(self, corner_radius=12)
        self.current_config_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 20), pady=20)
        self.current_config_frame.grid_columnconfigure(0, weight=1)
        self.current_config_frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(
            self.current_config_frame, text="Configuración DNS Actual", font=self.header_font
        ).grid(row=0, column=0, sticky="w", padx=20, pady=(20, 15))

        self.dns_info_scroll_frame = ctk.CTkScrollableFrame(
            self.current_config_frame, fg_color="transparent"
        )
        self.dns_info_scroll_frame.grid(row=1, column=0, sticky="nsew", padx=15, pady=(0, 10))
        self.dns_info_scroll_frame.grid_columnconfigure(0, weight=1)

        self.build_dns_servers_card()
        self.build_remote_requests_card()

        self.delete_dns_button = ctk.CTkButton(
            self.current_config_frame,
            text="Eliminar Configuración DNS",
            fg_color="#c0392b",
            hover_color="#922b21",
            command=lambda : self.reset_dns_configuration()
        )
        self.delete_dns_button.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 20))

    def build_dns_servers_card(self):
        servers_card = ctk.CTkFrame(self.dns_info_scroll_frame, corner_radius=10)
        servers_card.grid(row=0, column=0, sticky="ew", pady=(0, 10), padx=4)
        servers_card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            servers_card, 
            text="Servidor DNS:",
            font=self.small_bold_font,
            anchor="w"
        ).grid(row=0, column=0, sticky="w", padx=15, pady=(15, 5))

        dns_config = self.controller.get_dns_configuration()

        row = 1

        static_ip_title = ctk.CTkLabel(
            servers_card,
            text="IP estáticas",
            font=self.small_bold_font
        )
        static_ip_title.grid(row=row, column=0, sticky="w", padx=15, pady=(5, 5))

        row += 1

        for server in dns_config["static_ips"]:
            ctk.CTkLabel(
                servers_card,
                text=server,
                font=self.small_font,
                anchor="w",
                text_color="gray70"
            ).grid(row=row, column=0, sticky="w", padx=15, pady=2)

            row += 1


        dynamic_ip_title = ctk.CTkLabel(
            servers_card,
            text="IP dinámicas",
            font=self.small_bold_font
        )
        dynamic_ip_title.grid(row=row, column=0, sticky="w", padx=15, pady=(10, 5))

        row += 1

        for server in dns_config["dynamic_ips"]:
            ctk.CTkLabel(
                servers_card,
                text=server,
                font=self.small_font,
                anchor="w",
                text_color="gray70"
            ).grid(row=row, column=0, sticky="w", padx=15, pady=2)

            row += 1

    def build_remote_requests_card(self):
        remote_requests_card = ctk.CTkFrame(self.dns_info_scroll_frame, corner_radius=10)
        remote_requests_card.grid(row=1, column=0, sticky="ew", pady=(0, 10), padx=4)
        remote_requests_card.grid_columnconfigure(0, weight=1)

        dns_config = self.controller.get_dns_configuration()

        ctk.CTkLabel(
            remote_requests_card,
            text="Permitir solicitudes remotas:",
            font=self.small_bold_font,
            anchor="w",
        ).grid(row=0, column=0, sticky="w", padx=15, pady=(15, 5))

        status = "Sí" if not dns_config["remote_request"] else "No"
                
        ctk.CTkLabel(
            remote_requests_card,
            text= status ,
            font=self.small_font,
            anchor="w",
            text_color="gray70",
        ).grid(row=1, column=0, sticky="w", padx=15, pady=(0, 15))
    
    def reset_dns_configuration(self):
        success, message = self.controller.reset_dns_configuration()
        self.show_message(message)
        
        if success:
            self.build_dns_servers_card()
            self.build_remote_requests_card()
