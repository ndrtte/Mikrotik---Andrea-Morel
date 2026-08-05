import customtkinter as ctk

class DhcpView(ctk.CTkFrame):
    def __init__(self, parent, controller, show_message, interface_util, pool_address):
        """
            Vista para la creacion y eliminar configuraciones DHCP Server
        """
        super().__init__(parent, fg_color="transparent")

        self.controller = controller
        self.show_message = show_message
        self.interface_util = interface_util
        self.pool_address = pool_address

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        self.title_font = ctk.CTkFont(family="Poppins", size=20, weight="bold")
        self.card_title_font = ctk.CTkFont(family="Poppins", size=16, weight="bold")
        self.label_font = ctk.CTkFont(family="Poppins", size=13)
        self.small_font = ctk.CTkFont(family="Poppins", size=12)
        self.small_bold_font = ctk.CTkFont(family="Poppins", size=12, weight="bold")

        self.card_style = {
            "corner_radius": 16,
            "fg_color": "#FDF2F8",
            "border_width": 1,
            "border_color": "#F8BBD0",
        }

        self.disabled_options = ["no", "yes"]

        self.selected_server = ctk.StringVar(value="")

        self.build_title()
        self.build_left_column()
        self.build_right_column()

    def build_title(self):
        title = ctk.CTkLabel(
            self,
            text="DHCP Server",
            font=self.title_font,
            text_color="#C2185B"
        )
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=20, pady=(20, 0))

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

    def build_left_column(self):
        left_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        left_frame.grid(row=1, column=0, sticky="nsew", padx=(20, 10), pady=(10, 20))
        left_frame.grid_columnconfigure(0, weight=1)

        self.build_pool_card(left_frame)
        self.build_network_card(left_frame)
        self.build_server_card(left_frame)

    def build_pool_card(self, parent):
        pool_card = ctk.CTkFrame(parent, **self.card_style)
        pool_card.grid(row=0, column=0, sticky="ew", pady=(0, 15))
        pool_card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(pool_card, text="IP Pool", font=self.card_title_font, text_color="#880E4F").grid(
            row=0, column=0, sticky="w", padx=20, pady=(15, 10)
        )

        ctk.CTkLabel(pool_card, text="Nombre del Pool", font=self.label_font, text_color="#AD1457").grid(
            row=1, column=0, sticky="w", padx=20
        )
        self.pool_name_entry = ctk.CTkEntry(pool_card, placeholder_text="pool_lan", font=self.label_font)
        self.pool_name_entry.grid(row=2, column=0, sticky="ew", padx=20, pady=(2, 10))

        ctk.CTkLabel(pool_card, text="Rango de direcciones", font=self.label_font, text_color="#AD1457").grid(
            row=3, column=0, sticky="w", padx=20
        )
        self.pool_range_entry = ctk.CTkEntry(
            pool_card, placeholder_text="192.168.1.100-192.168.1.200", font=self.label_font
        )
        self.pool_range_entry.grid(row=4, column=0, sticky="ew", padx=20, pady=(2, 15))

        self.create_pool_button = ctk.CTkButton(
            pool_card, text="Crear Pool",
            fg_color="#EC407A", hover_color="#C2185B",
            font=self.label_font,
            command=lambda: self.create_pool()
        )
        self.create_pool_button.grid(row=5, column=0, sticky="ew", padx=20, pady=(0, 20))

    def build_network_card(self, parent):
        network_card = ctk.CTkFrame(parent, **self.card_style)
        network_card.grid(row=1, column=0, sticky="ew", pady=(0, 15))
        network_card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(network_card, text="Red DHCP", font=self.card_title_font, text_color="#880E4F").grid(
            row=0, column=0, sticky="w", padx=20, pady=(15, 10)
        )

        ctk.CTkLabel(network_card, text="Red", font=self.label_font, text_color="#AD1457").grid(
            row=1, column=0, sticky="w", padx=20
        )
        self.network_address_entry = ctk.CTkEntry(network_card, placeholder_text="192.168.1.0/24", font=self.label_font)
        self.network_address_entry.grid(row=2, column=0, sticky="ew", padx=20, pady=(2, 10))

        ctk.CTkLabel(network_card, text="Gateway", font=self.label_font, text_color="#AD1457").grid(
            row=3, column=0, sticky="w", padx=20
        )
        self.gateway_entry = ctk.CTkEntry(network_card, placeholder_text="192.168.1.1", font=self.label_font)
        self.gateway_entry.grid(row=4, column=0, sticky="ew", padx=20, pady=(2, 10))

        ctk.CTkLabel(network_card, text="DNS Server", font=self.label_font, text_color="#AD1457").grid(
            row=5, column=0, sticky="w", padx=20
        )
        self.dns_server_entry = ctk.CTkEntry(network_card, placeholder_text="8.8.8.8", font=self.label_font)
        self.dns_server_entry.grid(row=6, column=0, sticky="ew", padx=20, pady=(2, 15))

        self.create_network_button = ctk.CTkButton(
            network_card, text="Crear Network",
            fg_color="#EC407A", hover_color="#C2185B",
            font=self.label_font,
            command=lambda: self.create_dhcp_network()
        )
        self.create_network_button.grid(row=7, column=0, sticky="ew", padx=20, pady=(0, 20))

    def build_server_card(self, parent):
        server_card = ctk.CTkFrame(parent, **self.card_style)
        server_card.grid(row=2, column=0, sticky="ew")
        server_card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(server_card, text="DHCP Server", font=self.card_title_font, text_color="#880E4F").grid(
            row=0, column=0, sticky="w", padx=20, pady=(15, 10)
        )

        ctk.CTkLabel(server_card, text="Nombre", font=self.label_font, text_color="#AD1457").grid(
            row=1, column=0, sticky="w", padx=20
        )
        self.server_name_entry = ctk.CTkEntry(server_card, placeholder_text="dhcp_lan", font=self.label_font)
        self.server_name_entry.grid(row=2, column=0, sticky="ew", padx=20, pady=(2, 10))

        ctk.CTkLabel(server_card, text="Interfaz", font=self.label_font, text_color="#AD1457").grid(
            row=3, column=0, sticky="w", padx=20
        )

        success, interface_values = self.interface_util.get_all_interfaces()

        if not success:
            interface_values = []
            self.show_message(f"Error cargando interfaces: {interface_values}")

        self.interface_combobox = ctk.CTkComboBox(server_card, values=interface_values, font=self.label_font)
        self.interface_combobox.grid(row=4, column=0, sticky="ew", padx=20, pady=(2, 10))

        ctk.CTkLabel(server_card, text="Pool de direcciones", font=self.label_font, text_color="#AD1457").grid(
            row=5, column=0, sticky="w", padx=20
        )

        self.address_pool_combobox = ctk.CTkComboBox(
            server_card,
            values=[],
            font=self.label_font
        )

        self.address_pool_combobox.grid(
            row=6,
            column=0,
            sticky="ew",
            padx=20,
            pady=(2, 10)
        )

        self.refresh_pool_options()

        ctk.CTkLabel(server_card, text="Deshabilitado", font=self.label_font, text_color="#AD1457").grid(
            row=7, column=0, sticky="w", padx=20
        )
        self.disabled_combobox = ctk.CTkComboBox(server_card, values=self.disabled_options, font=self.label_font)
        self.disabled_combobox.grid(row=8, column=0, sticky="ew", padx=20, pady=(2, 15))

        self.create_server_button = ctk.CTkButton(
            server_card, text="Crear Servidor DHCP",
            fg_color="#EC407A", hover_color="#C2185B",
            font=self.label_font,
            command=lambda: self.create_dhcp_server()
        )
        self.create_server_button.grid(row=9, column=0, sticky="ew", padx=20, pady=(0, 20))

    def build_right_column(self):
        right_frame = ctk.CTkFrame(self, **self.card_style)
        right_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 20), pady=(10, 20))
        right_frame.grid_columnconfigure(0, weight=1)
        right_frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(right_frame, text="Servidores DHCP", font=self.card_title_font, text_color="#880E4F").grid(
            row=0, column=0, sticky="w", padx=20, pady=(15, 10)
        )

        self.server_list_frame = ctk.CTkScrollableFrame(right_frame, fg_color="transparent")
        self.server_list_frame.grid(row=1, column=0, sticky="nsew", padx=15, pady=(0, 10))
        self.server_list_frame.grid_columnconfigure(0, weight=1)

        self.load_server_list()

        self.delete_selected_button = ctk.CTkButton(
            right_frame,
            text="Eliminar seleccionado",
            fg_color="#C62828",
            hover_color="#8E0000",
            font=self.label_font,
            command=lambda: self.delete_dhcp_server()
        )
        self.delete_selected_button.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 20))

    #Aca de encarga de cargar los servidores que ya existen, se invoca en mas funciones como leimianr y crear para actualizar
    def load_server_list(self):
        for widget in self.server_list_frame.winfo_children():
            widget.destroy()

        servers = self.controller.get_all_dhcp_servers()

        for index, server in enumerate(servers):
            self.build_server_item(index, server)

    def build_server_item(self, index, server):
        item_frame = ctk.CTkFrame(self.server_list_frame, fg_color="#FFFFFF", corner_radius=10)
        item_frame.grid(row=index, column=0, sticky="ew", pady=6, padx=4)
        item_frame.grid_columnconfigure(1, weight=1)

        status = "Activo" if not server["status"] else "Deshabilitado"
        status_color = "#2E7D32" if not server["status"] else "#C62828"

        radio_button = ctk.CTkRadioButton(
            item_frame,
            text="",
            variable=self.selected_server,
            value=server["name"],
            fg_color="#EC407A",
            hover_color="#C2185B",
            width=20,
        )
        radio_button.grid(row=0, column=0, rowspan=4, padx=(15, 10), pady=15)

        ctk.CTkLabel(
            item_frame, text=server["name"], font=self.label_font, text_color="#880E4F", anchor="w"
        ).grid(row=0, column=1, sticky="w", padx=(0, 15), pady=(15, 2))

        ctk.CTkLabel(
            item_frame,
            text=f"Interfaz: {server['interface']}",
            font=self.small_font,
            text_color="#6A1B9A",
            anchor="w",
        ).grid(row=1, column=1, sticky="w", padx=(0, 15))

        ctk.CTkLabel(
            item_frame,
            text=f"Pool de direcciones: {server['pool']}",
            font=self.small_font,
            text_color="#6A1B9A",
            anchor="w",
        ).grid(row=2, column=1, sticky="w", padx=(0, 15))

        ctk.CTkLabel(
            item_frame,
            text=status,
            font=self.small_bold_font,
            text_color=status_color,
            anchor="w",
        ).grid(row=3, column=1, sticky="w", padx=(0, 15), pady=(2, 15))


    def create_pool(self):
        pool_name = self.pool_name_entry.get()
        pool_ranges = self.pool_range_entry.get()

        success, message = self.pool_address.create_ip_pool(
            pool_name,
            pool_ranges
        )

        self.show_message(message)

        if success:
            self.pool_name_entry.delete(0, "end")
            self.pool_range_entry.delete(0, "end")
            self.refresh_pool_options()

    #Estos es para para refrescar las opciones del pool si creo uno invoco esta funcion para actualziarlo, como algo asincrono
    def refresh_pool_options(self):
        success, address_pools = self.pool_address.get_pool()
        if success:
            self.address_pool_combobox.configure(values=address_pools)
            if address_pools:
                self.address_pool_combobox.set(address_pools[0])


    def create_dhcp_network(self):
        dhcp_address = self.network_address_entry.get()
        dhcp_gateway = self.gateway_entry.get()
        dns_ip = self.dns_server_entry.get()
        success, message = self.controller.create_dhcp_network(dhcp_address, dhcp_gateway, dns_ip)
        self.show_message(message)

        if success:
            self.network_address_entry.delete(0, "end")
            self.gateway_entry.delete(0, "end")
            self.dns_server_entry.delete(0, "end")

    def create_dhcp_server(self):
        server_name = self.server_name_entry.get()
        interface = self.interface_combobox.get()
        pool = self.address_pool_combobox.get()
        disabled = self.disabled_combobox.get()

        success, message = self.controller.create_dhcp_server(server_name, interface, pool, disabled)

        self.show_message(message)
        if success:
            self.server_name_entry.delete(0, "end")
            self.load_server_list()

    def delete_dhcp_server(self):
        server_name = self.selected_server.get()

        if not server_name:
            self.show_message("Seleccione un servidor DHCP.")
            return

        success, message = self.controller.delete_dhcp_server(server_name)

        self.show_message(message)

        if success:
            self.load_server_list()