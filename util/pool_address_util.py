class PoolAddressUtil:
    def __init__(self, session):
        self.session = session
    
    def create_ip_pool(self, pool_name, pool_ranges):
        pool_api = self.session.api.path("ip","pool")
        
        if not pool_name or not pool_ranges :
            return False, "Ingresa todos los campos"
            
        try:
            pool_api.add(
                name = pool_name,
                ranges = pool_ranges
            )
                
            return True, "Se ha creado el pool correctamente"
        except Exception as e:
            False, f"Hay un error de insercion: {e}"
    
    def get_pool(self):        
        try:
            pool_list = [
                u["name"]
                for u in self.session.api.path("ip","pool")
                if u.get("name")
            ]
            return True, pool_list
        except Exception as e:
            return False, str(e)