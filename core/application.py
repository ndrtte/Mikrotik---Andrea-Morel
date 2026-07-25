import customtkinter as ctk

from config import APP_NAME, WINDOW_HEIGHT, WINDOW_WIDTH

from views.connection_view import ConnectionView
from views.dashboard_view import RouterDashboardView
from views.router_name_view import RouterNameView
from views.ip_view import IpView
from views.dhcp_view import DhcpView

from services.router_session_service import RouterSession

from controller.connect_controller import ConnectController
from controller.router_name_controller import RouterNameController
from controller.ip_controller import IpController
from controller.dhcp_controller import DhcpController

from components.notifications import Notification

from util.interface_util import InterfaceUtil

class Application(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title(APP_NAME)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.session = RouterSession()

        self.connect_controller = ConnectController(self.session)

        self.router_name_controller = RouterNameController(self.session)
        
        self.ip_controller = IpController(self.session)

        self.dhcp_controller = DhcpController(self.session)
        
        self.interface_util = InterfaceUtil(self.session)
        
        self.view_container = ctk.CTkFrame(self)
        self.view_container.pack(
            fill="both",
            expand=True
        )

        self.notification = Notification(self)
        self.notification.pack(
            side="bottom",
            fill="x"
        )

        self.show_connection()

    def show_connection(self):
        self.clear_view()

        connection = ConnectionView(
            self.view_container,
            self.connect_controller,
            self.show_dashboard,
            self.show_message
        )

        connection.pack(fill="both", expand=True)

    def show_dashboard(self):
        self.clear_view()

        self.dashboard = RouterDashboardView(
            self.view_container,
            self.navigate
        )

        self.dashboard.pack(fill="both", expand=True)
        
        self.routes = {
            "router_name": lambda: RouterNameView(
                self.dashboard.view_container,
                self.router_name_controller,
                self.show_message
            ),
            "ip": lambda: IpView(
                self.dashboard.view_container,
                self.ip_controller,
                self.show_message,
                self.interface_util
            ),
            "dhcp": lambda: DhcpView(
                self.dashboard.view_container,
                self.dhcp_controller,
                self.show_message,
                self.interface_util
            )
        }
        
    def navigate(self, page):
            if page in self.routes:
                self.dashboard.load_view(
                    self.routes[page]()
                )

    def clear_view(self):
        for widget in self.view_container.winfo_children():
            widget.destroy()
    
    
    def show_message(self, message):
        self.notification.show(message)