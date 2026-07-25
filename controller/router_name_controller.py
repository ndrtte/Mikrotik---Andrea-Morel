class RouterNameController:

    def __init__(self, session):
        self.session = session


    def get_router_identity(self):
        try:
            identity = self.session.api.path("system", "identity")
            data = list(identity)

            return data[0]["name"]

        except Exception as e:
            print(e)
            return "Nombre vacio"
        

    def update_router_name(self, new_name):
        if not new_name:
            return False, "Ingresa un nombre valido"
        
        try:
            identity = self.session.api.path("system", "identity")

            tuple(identity(
                "set",
                name=new_name
            ))

            return True, "Nombre actualizado correctamente"

        except Exception as e:
            print("Error actualizando el nombre:", e)
            return False, str(e)
            
            