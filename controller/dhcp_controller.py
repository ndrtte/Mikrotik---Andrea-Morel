class DhcpController:
    def __init__(self, session):
        self.session = session
    
    def get_all_dhcp_servers(self):
        dhcp_api = self.session.api.path("ip","dhcp-server")
        
        dhcp_servers = dhcp_api.select()
            
        servers_list = []
            
        for server in dhcp_servers:
            servers_list.append({
                "name": server.get("name", "N/A"),
                "interface": server.get("interface", "N/A"),
                "pool": server.get("address-pool", "N/A"),
                "status": server.get("disabled", False)
            })
            
        return servers_list
    
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