import customtkinter as ctk
from views.router_name_view import RouterNameView
from views.ip_view import IpView

class RouterDashboardView(ctk.CTkFrame):
    """
    Vista para listar las opciones del menu
    """
    def __init__(self, parent, navigate):
        super().__init__(parent)
        self.navigate = navigate
        
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
        
        #En esta parte se utiliza un diciconario para definir las opciones del menu y a que corresponde sus vista (parte del /core/application.py)
        self.views = {
            "Asignar nombre a Router": "router_name",
            "Direcciones IP": "ip",
            "DHCP":"dhcp",
            "DNS" : "dns",
            "Rutas estaticas" : "static_routes",
            "Monitorear interfaces" : "interface_monitor",
            "Backups" : "backup"
        }

        #Aca recorro para mostrarlos en el meny y el command lambda es para que no se ejecute al menos a que yo haga click
        for item in self.views :
            ctk.CTkButton(
                self.sidebar,
                text=item,
                command=lambda i=item: self.navigate(self.views[i]) #en el application esta una parte que fine las vistas y qqui el navigate 
                                                                    #se busca mediante al valor de la clave por ejemplo self.view[DHCP] = "dhcp"
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

    #el padre de la subpantallas es el dashboard asi que aqui lo que hago es que secargue pero que se siga viendo el menu
    def load_view(self, view):

        self.content_label.pack_forget()

        if self.current_view:
            self.current_view.destroy()

        self.current_view = view
        self.current_view.pack(fill="both", expand=True)