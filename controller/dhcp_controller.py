class DhcpController:
    def __init__(self, session):
        self.session = session
    
    def get_all_dhcp_servers(self):
        dhcp_api = self.session.api.path("ip","dhcp-server") #aca lo mismo  /ip/dhcp-server
        
        dhcp_servers = dhcp_api.select() #esto es para hacerlo por medio de queries
            
        servers_list = []
            
        for server in dhcp_servers:
            servers_list.append({ #ir añadiendo las cosas mediante filtro de solo unso campos como nombre, interfaz, pool y si esta habilitada(valor boolean)
                "name": server.get("name", "N/A"),
                "interface": server.get("interface", "N/A"),
                "pool": server.get("address-pool", "N/A"),
                "status": server.get("disabled", False)
            })
            
        return servers_list
    
    #para crear la red dhcp si no existe
    def create_dhcp_network(self, dhcp_address, dhcp_gateway, dns_ip):
        dhcp_network_api = self.session.api.path("ip", "dhcp-server", "network")

        if not dhcp_address or not dhcp_gateway or not dns_ip:
            return False, "Completa todos los campos." #manejo de erroes

        try:
            dhcp_network_api.add(**{#utilizo esto porque la api no reconoce poner por ejemplo dns_server sino solo 'dns-server'
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
        
    def delete_dhcp_server(self, name):
        dhcp_api = self.session.api.path("ip", "dhcp-server")

        try:
            for server in dhcp_api:
                if server["name"] == name: #Mando a traer todas las dhcp en mikrotik y recorro hasta encontrar el id que necesito comparando mediante nombre
                    dhcp_api.remove(server[".id"])#remove es para el comando de eliminar
                    return True, "Servidor DHCP eliminado correctamente."

            return False, "No se encontró el servidor DHCP."

        except Exception as e:
            print(e)
            return False, f"Ocurrió un error al eliminar el servidor DHCP: {e}"
        