from librouteros import connect

class ConnectController:
    def __init__(self, session):
        self.session = session

    #De esta funcion vive toda la plaicacion, es la unica que directamente crea la conexion con librouteros
    def connect_router(self, ip, username, password):
        try:
            api = connect(
                host=ip,
                username=username,
                password=password
            )

            self.session.set_connection(api) #para la sesion se hace un set para que ahora el valor de coenxion sea session y que se conexte en todos los controladores

            return True, "Conexión exitosa con el router"

        except Exception as e:
            print(f"Error de conexión: {e}")

            return False, "No se pudo conectar con el router"
