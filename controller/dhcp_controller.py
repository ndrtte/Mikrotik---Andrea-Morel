class DhcpController:
    def __init__(self, session):
        self.session = session
    
    def get_all_dhcp_servers(self):
        dhcp_api = self.session.api.path("ip","dhcp-server")
        
        try :
            dhcp_servers = dhcp_api.select()
            
            servers_list = []
            
            for server in dhcp_servers:
                servers_list.append({
                    "name" : server.get("name","N/A"),
                    "interface" : server.get("interface", "N/A"),
                    "pool_name" : server.get("address-pool", "N/A"),
                    "status" : server.get("disabled", "False")
                })
            
            return True, servers_list
        
        except Exception as e:
            return False, str(e)
        