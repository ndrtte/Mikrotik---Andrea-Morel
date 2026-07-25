import customtkinter as ctk
from views.router_name_view import RouterNameView

class RouterDashboardView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid(row=0, column=0, sticky="nsew")

        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nswe")

        self.sidebar_label = ctk.CTkLabel(
            self.sidebar,
            text="Menú",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.sidebar_label.pack(pady=10)

        self.current_view = None
        
        self.views = {
            "Asignar nombre a Router": RouterNameView,
            #"Direcciones IP": IpView,
            #"DHCP": DhcpView,
            #"DNS": DnsView,
            #"Rutas estáticas": StaticRoutesView,
            #"Interfaces": InterfacesView,
            #"Respaldo": BackupView
        }

        for item in self.views :
            ctk.CTkButton(
                self.sidebar,
                text=item,
                command=lambda i=item: self.load_view(i)
            ).pack(pady=5, fill="x")


        self.content = ctk.CTkFrame(self)
        self.content.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        self.content_label = ctk.CTkLabel(
            self.content,
            text="Selecciona una opción del menú"
        )
        self.content_label.pack(pady=20)

        self.view_container = ctk.CTkFrame(self.content)
        self.view_container.pack(fill="both", expand=True)

    def load_view(self, option):

        self.content_label.pack_forget()

        if self.current_view:
            self.current_view.destroy()

        view = self.views.get(option)

        if view:
            self.current_view = view(self.view_container)
            self.current_view.pack(fill="both", expand=True)