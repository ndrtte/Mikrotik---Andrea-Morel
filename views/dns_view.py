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

        self.current_dns_servers = ["8.8.8.8", "1.1.1.1"]
        self.current_allow_remote_requests = "Sí"

        self._build_left_column()
        self._build_right_column()

    def _build_left_column(self):
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

    def _build_right_column(self):
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

        self._build_dns_servers_card()
        self._build_remote_requests_card()

        self.delete_dns_button = ctk.CTkButton(
            self.current_config_frame,
            text="Eliminar Configuración DNS",
            fg_color="#c0392b",
            hover_color="#922b21",
        )
        self.delete_dns_button.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 20))

    def _build_dns_servers_card(self):
        servers_card = ctk.CTkFrame(self.dns_info_scroll_frame, corner_radius=10)
        servers_card.grid(row=0, column=0, sticky="ew", pady=(0, 10), padx=4)
        servers_card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            servers_card, text="Servidor DNS:", font=self.small_bold_font, anchor="w"
        ).grid(row=0, column=0, sticky="w", padx=15, pady=(15, 5))

        for index, server in enumerate(self.current_dns_servers):
            ctk.CTkLabel(
                servers_card, text=server, font=self.small_font, anchor="w", text_color="gray70"
            ).grid(row=index + 1, column=0, sticky="w", padx=15, pady=(0, 5 if index < len(self.current_dns_servers) - 1 else 15))

    def _build_remote_requests_card(self):
        remote_requests_card = ctk.CTkFrame(self.dns_info_scroll_frame, corner_radius=10)
        remote_requests_card.grid(row=1, column=0, sticky="ew", pady=(0, 10), padx=4)
        remote_requests_card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            remote_requests_card,
            text="Allow Remote Requests:",
            font=self.small_bold_font,
            anchor="w",
        ).grid(row=0, column=0, sticky="w", padx=15, pady=(15, 5))

        ctk.CTkLabel(
            remote_requests_card,
            text=self.current_allow_remote_requests,
            font=self.small_font,
            anchor="w",
            text_color="gray70",
        ).grid(row=1, column=0, sticky="w", padx=15, pady=(0, 15))
