class IpController:
    def __init__(self, session):
        self.session = session
        
    def get_all_ip(self):
        
        ip_list = []

        try:
            ip_api = self.session.api.path("ip", "address")

            for ip in ip_api:
                ip_list.append({
                    "ip": ip.get("address"),
                    "network": ip.get("network"),
                    "interface": ip.get("interface")
                })

            return True, ip_list

        except Exception as e:
            return False, str(e)
    
    def create_ip(self, ip, target_interface):
        try:
            ip_api = self.session.api.path("ip", "address")
            ip_api.add(address=ip, interface = target_interface)
            
            return True, "Se agrego la ip con exito"
        except Exception as e:
            return False, str(e)   
    
    def delete_ip(self, ip):
        try:
            ip_api = self.session.api.path("ip", "address")
            record_id = None

            for record in ip_api:
                if record.get("address") == ip:
                    record_id = record.get(".id")
                    break

            if record_id is None:
                return False, f"No se encontró la IP {ip}"

            ip_api.remove(record_id)

            return True, f"Se eliminó con éxito la IP {ip}"

        except Exception as e:
            return False, str(e)