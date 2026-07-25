import customtkinter as ctk

from config import APP_NAME, WINDOW_HEIGHT, WINDOW_WIDTH
from views.connection_view import ConnectionView
from views.dashboard_view import RouterDashboardView
from services.router_session_service import RouterSession
from controller.connect_controller import ConnectController
from controller.router_name_controller import RouterNameController
from components.notifications import Notification

class Application(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title(APP_NAME)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.session = RouterSession()

        self.connect_controller = ConnectController(self.session)

        self.router_controller = RouterNameController(self.session)
        
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
            self.show_dashboard
        )

        connection.pack(fill="both", expand=True)

    def show_dashboard(self):
        self.clear_view()

        dashboard = RouterDashboardView(
            self.view_container,
            self.router_controller
        )

        dashboard.pack(fill="both", expand=True)

    def clear_view(self):
        for widget in self.view_container.winfo_children():
            widget.destroy()
    
    def show_message(self, message):
        self.notification.show(message)