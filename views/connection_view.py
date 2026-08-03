import customtkinter as ctk

class ConnectionView(ctk.CTkFrame):
    def __init__(self, parent, controller, on_success, show_message):

        self.controller = controller
        self.on_success = on_success
        self.show_message = show_message
        super().__init__(parent, fg_color="transparent")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        card = ctk.CTkFrame(
            self, corner_radius=16,
            fg_color="#FDF2F8", border_width=1, border_color="#F8BBD0"
        )
        card.grid(row=0, column=0)
        card.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            card,
            text="Conectar a MikroTik",
            font=ctk.CTkFont(family="Poppins", size=20, weight="bold"),
            text_color="#C2185B"
        )

        title.grid(row=0, column=0, padx=40, pady=(30, 4))

        subtitle = ctk.CTkLabel(
            card,
            text="Ingresa los datos de tu router",
            font=ctk.CTkFont(family="Poppins", size=12),
            text_color="#AD1457"
        )

        subtitle.grid(row=1, column=0, padx=40, pady=(0, 25))

        self.ip_entry = self.build_field(card, "Dirección IP", "192.168.88.1", row=2)
        self.user_entry = self.build_field(card, "Usuario", "admin", row=4)
        self.password_entry = self.build_field(card, "Contraseña", "••••••••", row=6, show="*")

        self.status_label = ctk.CTkLabel(
            card, text="", font=ctk.CTkFont(family="Poppins", size=11)
        )
        self.status_label.grid(row=8, column=0, pady=(4, 0))

        button = ctk.CTkButton(
            card,
            text="Conectar",
            height=40,
            fg_color="#EC407A", hover_color="#C2185B",
            font=ctk.CTkFont(family="Poppins", size=14, weight="bold"),
            command=self.on_connect
        )
        button.grid(row=9, column=0, padx=40, pady=(16, 30), sticky="ew")

    def build_field(self, parent, label_text, placeholder, row, show=None):
        label = ctk.CTkLabel(
            parent,
            text=label_text,
            font=ctk.CTkFont(family="Poppins", size=12, weight="bold"),
            text_color="#880E4F",
            anchor="w"
        )

        label.grid(row=row, column=0, padx=40, pady=(0, 4), sticky="ew")

        entry = ctk.CTkEntry(
            parent,
            placeholder_text=placeholder,
            height=36,
            font=ctk.CTkFont(family="Poppins", size=13),
            show=show
        )
        entry.grid(row=row + 1, column=0, padx=40, pady=(0, 12), sticky="ew")
        return entry

    def on_connect(self):

        ip = self.ip_entry.get()
        user = self.user_entry.get()
        password = self.password_entry.get()

        success, message = self.controller.connect_router(
            ip,
            user,
            password
        )

        self.status_label.configure(
            text=message,
            text_color="#2E7D32" if success else "#C62828"
        )
        self.show_message(message)

        if success:
            self.on_success()