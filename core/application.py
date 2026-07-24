import customtkinter as ctk

from config import APP_NAME, WINDOW_HEIGHT, WINDOW_WIDTH
from views.connection_view import ConnectionView
from views.dashboard_view import RouterDashboardView

class Application(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title(APP_NAME)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.show_connection()

    def show_connection(self):
        self.clear_view()

        connection = ConnectionView(self)
        connection.pack(fill="both", expand=True)

    def show_dashboard(self):
        self.clear_view()

        dashboard = RouterDashboardView(self)
        dashboard.pack(fill="both", expand=True)

    def clear_view(self):
        for widget in self.winfo_children():
            widget.destroy()