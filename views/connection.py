import customtkinter as ctk
from services.mikrotik_services import MikroTikService

class ConnectionView(ctk.CTkFrame):
    def __init__(self, parent):
        self.router_service = MikroTikService()
        super().__init__(parent, fg_color="transparent")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        card = ctk.CTkFrame(self, corner_radius=16)
        card.grid(row=0, column=0)
        card.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            card,
            text="Conectar a MikroTik",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        
        title.grid(row=0, column=0, padx=40, pady=(30, 4))

        subtitle = ctk.CTkLabel(
            card,
            text="Ingresa los datos de tu router",
            font=ctk.CTkFont(size=12),
            text_color=("#A587AA", "#C79AB8")
        )
        
        subtitle.grid(row=1, column=0, padx=40, pady=(0, 25))

        self.ip_entry = self._build_field(card, "Dirección IP", "192.168.88.1", row=2)
        self.user_entry = self._build_field(card, "Usuario", "admin", row=4)
        self.password_entry = self._build_field(card, "Contraseña", "••••••••", row=6, show="*")

        self.status_label = ctk.CTkLabel(card, text="", font=ctk.CTkFont(size=11))
        self.status_label.grid(row=8, column=0, pady=(4, 0))

        button = ctk.CTkButton(
            card,
            text="Conectar",
            height=40,
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.on_connect
        )
        button.grid(row=9, column=0, padx=40, pady=(16, 30), sticky="ew")

    def _build_field(self, parent, label_text, placeholder, row, show=None):
        label = ctk.CTkLabel(
            parent,
            text=label_text,
            font=ctk.CTkFont(size=12, weight="bold"),
            anchor="w"
        )
        
        label.grid(row=row, column=0, padx=40, pady=(0, 4), sticky="ew")

        entry = ctk.CTkEntry(
            parent,
            placeholder_text=placeholder,
            height=36,
            show=show
        )
        entry.grid(row=row + 1, column=0, padx=40, pady=(0, 12), sticky="ew")
        return entry

    def on_connect(self):

        ip = self.ip_entry.get()
        user = self.user_entry.get()
        password = self.password_entry.get()

        success, result = self.router_service.connect_router(
            ip,
            user,
            password
        )

        if success:
            print("Conectado correctamente")
            print(result)

            #self.show_dashboard()

        else:
            print("Error de conexión:")
            print(result)
        