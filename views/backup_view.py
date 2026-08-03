import customtkinter as ctk


class BackupView(ctk.CTkFrame):
    """
    Vista para listar y crear backups del router.
    """

    REFRESH_INTERVAL_MS = 5000  # cada 5 segundos

    def __init__(self, parent, controller, show_message):
        super().__init__(parent, fg_color="transparent")

        self.controller = controller
        self.show_message = show_message

        self.name_entry = None
        self.password_entry = None
        self.backups_container = None
        self.after_id = None

        self.build_ui()
        self.start_auto_refresh()

    def build_ui(self):
        title = ctk.CTkLabel(
            self,
            text="Backups",
            font=ctk.CTkFont(family="Poppins", size=20, weight="bold"),
            text_color="#C2185B"
        )
        title.pack(pady=(10, 20), anchor="w", padx=20)

        self.build_create_form()

        list_title = ctk.CTkLabel(
            self, text="Backups existentes",
            font=ctk.CTkFont(family="Poppins", size=15, weight="bold"),
            text_color="#880E4F"
        )
        list_title.pack(anchor="w", padx=20, pady=(10, 5))

        self.backups_container = ctk.CTkScrollableFrame(
            self, fg_color="#FDF2F8", corner_radius=16
        )
        self.backups_container.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    def build_create_form(self):
        form_card = ctk.CTkFrame(
            self, corner_radius=16,
            fg_color="#FDF2F8", border_width=1, border_color="#F8BBD0"
        )
        form_card.pack(fill="x", padx=20, pady=(0, 15))

        form_title = ctk.CTkLabel(
            form_card, text="Crear nuevo backup",
            font=ctk.CTkFont(family="Poppins", size=15, weight="bold"),
            text_color="#880E4F"
        )
        form_title.pack(pady=(15, 10), padx=15, anchor="w")

        self.name_entry = ctk.CTkEntry(
            form_card, placeholder_text="Nombre del backup",
            font=ctk.CTkFont(family="Poppins", size=13)
        )
        self.name_entry.pack(fill="x", padx=15, pady=5)

        self.password_entry = ctk.CTkEntry(
            form_card, placeholder_text="Contraseña (opcional)", show="*",
            font=ctk.CTkFont(family="Poppins", size=13)
        )
        self.password_entry.pack(fill="x", padx=15, pady=5)

        create_button = ctk.CTkButton(
            form_card, text="Crear backup",
            fg_color="#EC407A", hover_color="#C2185B",
            font=ctk.CTkFont(family="Poppins", size=13, weight="bold"),
            command=self.handle_create_backup
        )
        create_button.pack(padx=15, pady=(10, 15), anchor="w")

    def handle_create_backup(self):
        name = self.name_entry.get().strip()
        password = self.password_entry.get().strip()

        success, message = self.controller.create_backup(name=name, password=password)

        self.show_message(message)

        if success:
            self.name_entry.delete(0, "end")
            self.password_entry.delete(0, "end")
            self.load_backups()

    def start_auto_refresh(self):
        self.load_backups()
        self.after_id = self.after(self.REFRESH_INTERVAL_MS, self.start_auto_refresh)

    def stop_auto_refresh(self):
        if self.after_id is not None:
            self.after_cancel(self.after_id)
            self.after_id = None

    def destroy(self):
        self.stop_auto_refresh()
        super().destroy()

    def load_backups(self):
        for widget in self.backups_container.winfo_children():
            widget.destroy()

        backups = self.controller.get_backups()

        if not backups:
            empty_label = ctk.CTkLabel(
                self.backups_container, text="No hay backups disponibles",
                font=ctk.CTkFont(family="Poppins", size=13),
                text_color="#AD1457"
            )
            empty_label.pack(pady=20)
            return

        for backup in backups:
            self.create_backup_row(backup)

    def create_backup_row(self, backup):
        row = ctk.CTkFrame(self.backups_container, fg_color="#FFFFFF", corner_radius=10)
        row.pack(fill="x", padx=5, pady=5)

        name_label = ctk.CTkLabel(
            row, text=backup.get("name", "--"),
            font=ctk.CTkFont(family="Poppins", size=13, weight="bold"),
            text_color="#880E4F"
        )
        name_label.pack(side="left", padx=10, pady=10)

        details_label = ctk.CTkLabel(
            row,
            text=f"{backup.get('size', '--')} bytes | {backup.get('last_modified', '--')}",
            font=ctk.CTkFont(family="Poppins", size=12),
            text_color="#6A1B9A"
        )
        details_label.pack(side="right", padx=10, pady=10)