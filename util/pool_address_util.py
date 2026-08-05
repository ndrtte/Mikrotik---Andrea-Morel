class PoolAddressUtil:
    def __init__(self, session):
        self.session = session
    
    #Estes util es para separar responsabilidades ya que crear un pool es independiente de crear DHCP, un pool se puede crear por muchas razones mas
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
            False, f"Hay un error de insercion: {str(e)}"
    
    #Para cargarlas en los vista de DHCP
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