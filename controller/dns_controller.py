class DnsController:
    def __init__(self, session):
        self.session = session
        
    def get_dns_configuration(self):
        dns_api = self.session.api.path("ip", "dns")

        try:
            data = list(dns_api)[0]

            return {
                "static_ips": data.get("servers", "").split(","), #esto es porque viene con comas y yo las quiero en formato lista por asi decirlo
                "dynamic_ips": data.get("dynamic-servers", "").split(","), #igual aca
                "remote_request": data.get("allow-remote-requests") #yes o no valor
            }

        except Exception as e:
            return print(e)

    def reset_dns_configuration(self):
        try:
            dns_api = self.session.api.path("ip", "dns")

            dns_api.update(#aca solo modifico la configuraicon, no elimino nada
                servers="",#limpio las ips
                **{"allow-remote-requests": False} #y esto es false que son los valores predterminados
            )
            
            return True, "DNS reseteado correctamente."

        except Exception as e:
            return False, f"Error al resetear DNS: {str(e)}"
        
    def update_dns_configuration(self, ip_servers, allow_remote_requests):
        try:
            dns_api = self.session.api.path("ip", "dns")#aca si actualizo las ips

            dns_api.update(
                servers=ip_servers, #aca son todas las ips separadas por coma
                **{"allow-remote-requests": allow_remote_requests} #aca solo pongo yes o no
            )

            return True, "Se ha actualizado la configuración del DNS correctamente."

        except Exception as e:
            return False, f"Error al actualizar DNS: {str(e)}"