class IpController:
    def __init__(self, session):
            self.session = session
    
    def get_all_interfaces(self):
        try:
            #Lo que devuelve esto es un lista de diccionario entonces aqui
            #hago que se filtre solo los valores de la clave 'name' y por si acaso no hay interfaces entonces da None
            interfaces = [
                u["name"]
                for u in self.session.api.path("interface")
                if u.get("name")
            ]

            return True, interfaces

        except Exception as e:
            return False, str(e)
        
            