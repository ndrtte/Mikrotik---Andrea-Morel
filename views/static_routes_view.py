import customtkinter as ctk

class StaticRoutesViews(ctk.CTkFrame):
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
        self.add_frame = ctk.CTkFrame(self, corner_radius=12)
        self.add_frame.grid(row=0, column=0, sticky="nsew", padx=(20, 10), pady=20)
        self.add_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self.add_frame, text="Agregar Ruta Estática", font=self.header_font
        ).grid(row=0, column=0, sticky="w", padx=20, pady=(20, 15))

        ctk.CTkLabel(self.add_frame, text="Destino (red/máscara)", font=self.label_font).grid(
            row=1, column=0, sticky="w", padx=20
        )
        self.dest_entry = ctk.CTkEntry(self.add_frame, placeholder_text="192.168.1.0/24")
        self.dest_entry.grid(row=2, column=0, sticky="ew", padx=20, pady=(2, 15))

        ctk.CTkLabel(self.add_frame, text="Gateway (IP)", font=self.label_font).grid(
            row=3, column=0, sticky="w", padx=20
        )
        self.gateway_entry = ctk.CTkEntry(self.add_frame, placeholder_text="10.0.0.1")
        self.gateway_entry.grid(row=4, column=0, sticky="ew", padx=20, pady=(2, 15))

        ctk.CTkLabel(self.add_frame, text="Comentario (opcional)", font=self.label_font).grid(
            row=5, column=0, sticky="w", padx=20
        )
        self.comment_entry = ctk.CTkEntry(self.add_frame, placeholder_text="Ej: Red LAN")
        self.comment_entry.grid(row=6, column=0, sticky="ew", padx=20, pady=(2, 25))

        # Botón agregar
        self.add_button = ctk.CTkButton(
            self.add_frame, text="Agregar Ruta",
            command=self.add_static_route
        )
        self.add_button.grid(row=7, column=0, sticky="ew", padx=20, pady=(0, 20))

    def build_right_column(self):
        self.list_frame = ctk.CTkFrame(self, corner_radius=12)
        self.list_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 20), pady=20)
        self.list_frame.grid_columnconfigure(0, weight=1)
        self.list_frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(
            self.list_frame, text="Rutas Estáticas Actuales", font=self.header_font
        ).grid(row=0, column=0, sticky="w", padx=20, pady=(20, 15))

        self.routes_scroll = ctk.CTkScrollableFrame(
            self.list_frame, fg_color="transparent"
        )
        self.routes_scroll.grid(row=1, column=0, sticky="nsew", padx=15, pady=(0, 10))
        self.routes_scroll.grid_columnconfigure(0, weight=1)

        self.delete_button = ctk.CTkButton(
            self.list_frame,
            text="Eliminar Ruta Seleccionada",
            fg_color="#c0392b",
            hover_color="#922b21",
            command=self.delete_selected_route
        )
        self.delete_button.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 20))

        self.selected_route_id = ctk.StringVar(value="")

        self.load_routes()

    def load_routes(self):
        for widget in self.routes_scroll.winfo_children():
            widget.destroy()

        routes = self.controller.get_static_routes()
        if not routes:
            ctk.CTkLabel(
                self.routes_scroll,
                text="No hay rutas estáticas configuradas.",
                font=self.small_font,
                text_color="gray70"
            ).grid(row=0, column=0, padx=10, pady=10)
            return

        for idx, route in enumerate(routes):
            self.create_route_card(route, idx)

    def create_route_card(self, route, index):
        card = ctk.CTkFrame(self.routes_scroll, corner_radius=10)
        card.grid(row=index, column=0, sticky="ew", pady=(0, 10), padx=4)
        card.grid_columnconfigure(1, weight=1)

        card.route_id = route.get(".id")

        radio_button = ctk.CTkRadioButton(
            card,
            text="",
            variable=self.selected_route_id,
            value=card.route_id,
            width=20,
        )
        radio_button.grid(row=0, column=0, rowspan=3, padx=(15, 10), pady=15)

        dest_text = f"Destino: {route.get('dest', 'N/A')}"
        gateway_text = f"Gateway: {route.get('gateway', 'N/A')}"

        ctk.CTkLabel(
            card, text=dest_text, font=self.small_bold_font, anchor="w"
        ).grid(row=0, column=1, sticky="w", padx=(0, 15), pady=(10, 2))

        ctk.CTkLabel(
            card, text=gateway_text, font=self.small_font, anchor="w", text_color="gray70"
        ).grid(row=1, column=1, sticky="w", padx=(0, 15), pady=(0, 2))

        comment = route.get("comment")
        ctk.CTkLabel(
            card,
            text=f"Comentario: {comment}" if comment else "",
            font=self.small_font, anchor="w", text_color="gray60"
        ).grid(row=2, column=1, sticky="w", padx=(0, 15), pady=(0, 10))

    def delete_selected_route(self):
        route_id = self.selected_route_id.get()

        if not route_id:
            self.show_message("No hay ninguna ruta seleccionada.")
            return

        success, message = self.controller.delete_static_route(route_id)
        self.show_message(message)
        if success:
            self.selected_route_id.set("")
            self.load_routes()

    def add_static_route(self):
        dest = self.dest_entry.get().strip()
        gateway = self.gateway_entry.get().strip()
        comment = self.comment_entry.get().strip()

        if not dest or not gateway:
            self.show_message("Debe ingresar destino y gateway.")
            return

        success, message = self.controller.add_static_route(dest, gateway, comment)
        self.show_message(message)
        if success:
            self.dest_entry.delete(0, ctk.END)
            self.gateway_entry.delete(0, ctk.END)
            self.comment_entry.delete(0, ctk.END)
            self.load_routes()