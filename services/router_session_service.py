class RouterSession:

    def __init__(self):
        self.api = None

    #El obejto Session se setea con estas funciones 
    def set_connection(self, api):
        self.api = api

    #Para vericar la vida util de conexion
    def is_connected(self):
        return self.api is not None
    
    #Y desconexion
    def disconntect(self):
        if self.api:
            self.api.close()
            self.api = None