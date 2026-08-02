import customtkinter as ctk

class InterfaceMonitorView(ctk.CTkFrame):
    REFRESH_INTERVAL_MS = 2000
    def __init__(self, parent, controller, show_message, interface_util):
        super().__init__(parent, fg_color="transparent")

        self.controller = controller
        self.show_message = show_message
        self.interface_util = interface_util
        self.interface_names = []
        self._after_id = None
        self.interface_cards = {}

        self.load_interfaces()

        self.build_ui()
        self.start_monitoring()

    def build_ui(self):
        title = ctk.CTkLabel(
            self,
            text="Monitor de Interfaces",
            font=ctk.CTkFont(family="Poppins", size=20, weight="bold"),
            text_color="#C2185B"
        )
        title.pack(pady=(10, 20), anchor="w", padx=20)

        cards_container = ctk.CTkFrame(self, fg_color="transparent")
        cards_container.pack(fill="both", expand=True, padx=20)
        cards_container.grid_columnconfigure((0, 1), weight=1)

        for i, iface_name in enumerate(self.interface_names):
            card = self.create_interface_card(cards_container, iface_name)
            card.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")

    def create_interface_card(self, parent, iface_name):
        card = ctk.CTkFrame(
            parent, corner_radius=16,
            fg_color="#FDF2F8", border_width=1, border_color="#F8BBD0"
        )

        name_label = ctk.CTkLabel(
            card, text=iface_name,
            font=ctk.CTkFont(family="Poppins", size=16, weight="bold"),
            text_color="#880E4F"
        )
        name_label.pack(pady=(15, 5), padx=15, anchor="w")

        status_label = ctk.CTkLabel(
            card, text="Estado: --",
            font=ctk.CTkFont(family="Poppins", size=13),
            text_color="#AD1457"
        )
        status_label.pack(pady=2, padx=15, anchor="w")

        rx_label = ctk.CTkLabel(
            card, text="Tráfico entrada: --",
            font=ctk.CTkFont(family="Poppins", size=13),
            text_color="#6A1B9A"
        )
        rx_label.pack(pady=2, padx=15, anchor="w")

        tx_label = ctk.CTkLabel(
            card, text="Tráfico salida: --",
            font=ctk.CTkFont(family="Poppins", size=13),
            text_color="#6A1B9A"
        )
        tx_label.pack(pady=(2, 15), padx=15, anchor="w")

        self.interface_cards[iface_name] = {
            "status": status_label,
            "rx": rx_label,
            "tx": tx_label
        }

        return card

    def start_monitoring(self):
        self.refresh_data()

    def stop_monitoring(self):
        if self._after_id is not None:
            self.after_cancel(self._after_id)
            self._after_id = None

    def refresh_data(self):
        for iface_name in self.interface_names:
            self.update_interface(iface_name)

        self._after_id = self.after(self.REFRESH_INTERVAL_MS, self.refresh_data)

    def update_interface(self, iface_name):
        success, data = self.controller.get_interface_monitor(iface_name)
        card = self.interface_cards.get(iface_name)

        if not card:
            return

        if not success:
            card["status"].configure(text="Estado: Error", text_color="#C62828")
            self.show_message(f"Error al obtener {iface_name}: {data}")
            return

        status = data.get("status", "--")
        status_color = "#2E7D32" if status == "Up" else "#C62828"

        card["status"].configure(text=f"Estado: {status}", text_color=status_color)
        card["rx"].configure(text=f"Tráfico entrada: {data.get('rx', '--')}")
        card["tx"].configure(text=f"Tráfico salida: {data.get('tx', '--')}")

    def destroy(self):
        self.stop_monitoring()
        super().destroy()
        
    def load_interfaces(self):
        success, interfaces = self.interface_util.get_all_interfaces()
        if success:
            self.interface_names = interfaces[:2]