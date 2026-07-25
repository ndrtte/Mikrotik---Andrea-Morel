from librouteros import connect

class ConnectController:
    def __init__(self, session):
        self.session = session

    def connect_router(self, ip, username, password):
        try:
            api = connect(
                host=ip,
                username=username,
                password=password
            )

            self.session.set_connection(api)

            return True, "Conexión exitosa con el router"

        except Exception as e:
            print(f"Error de conexión: {e}")

            return False, "No se pudo conectar con el router"
