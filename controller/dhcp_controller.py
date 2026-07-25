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
    
    def create_dhcp_network(self, dhcp_address, dhcp_gateway, dns_ip):
        dhcp_network_api = self.session.api.path("ip", "dhcp-server", "network")

        if not dhcp_address or not dhcp_gateway or not dns_ip:
            return False, "Completa todos los campos."

        try:
            dhcp_network_api.add(**{
                "address": dhcp_address,
                "gateway": dhcp_gateway,
                "dns-server": dns_ip
            })

            return True, "Red DHCP creada correctamente."

        except Exception as e:
            print(e)
            return False, f"Ocurrió un error al crear la red DHCP: {str(e)}"
        
        
    def create_dhcp_server(self,dhcp_name, dhcp_interface, pool_name, status):
        
        dhcp_api = self.session.api.path("ip","dhcp-server")
        
        if not dhcp_name or not dhcp_interface or not pool_name or not status:
            return False, "Completa todos los campos"
        
        try:
            dhcp_api.add(**{
                "name": dhcp_name,
                "interface" : dhcp_interface,
                "address-pool" : pool_name,
                "disabled" : status
            })
            return True, "Servidor DHCP creado correctamente."
            
        except Exception as e:
            print(e)
            return False, f"Ocurrió un error al crear el servidor DHCP: {str(e)}"