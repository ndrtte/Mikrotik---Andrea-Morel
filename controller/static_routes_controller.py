class StaticRoutesController:
    def __init__(self, session):
        self.session = session

    def get_static_routes(self):
        try:
            route_api = self.session.api.path("ip", "route")
            routes = list(route_api)

            static_routes = []

            for route in routes:
                if route.get("dynamic") == "true":
                    continue

                static_routes.append({
                    "dest": route.get("dst-address"),
                    "gateway": route.get("gateway"),
                    "comment": route.get("comment", ""),
                    ".id": route.get(".id")
                })

            return static_routes

        except Exception as e:
            print(f"Error al obtener rutas estáticas: {e}")
            return []

    def add_static_route(self, dest, gateway, comment=""):
        try:
            route_api = self.session.api.path("ip", "route")
            route_api.add(
                **{
                    "dst-address": dest,
                    "gateway": gateway,
                    "comment": comment
                }
            )
            return True, "Ruta agregada correctamente."
        except Exception as e:
            return False, f"Error al agregar ruta: {str(e)}"

    def delete_static_route(self, route_id):
        try:
            route_api = self.session.api.path("ip", "route")
            route_api.remove(route_id)
            return True, "Ruta eliminada correctamente."
        except Exception as e:
            return False, f"Error al eliminar ruta: {str(e)}"