class DnsController:
    def __init__(self, session):
        self.session = session
        
    def get_dns_configuration(self):
        dns_api = self.session.api.path("ip", "dns")

        try:
            data = list(dns_api)[0]

            return {
                "static_ips": data.get("servers", "").split(","),
                "dynamic_ips": data.get("dynamic-servers", "").split(","),
                "remote_request": data.get("allow-remote-requests")
            }

        except Exception as e:
            return print(e)

    def reset_dns_configuration(self):
        try:
            dns_api = self.session.api.path("ip", "dns")

            dns_api.update(
                servers="",
                **{"allow-remote-requests": "no"}
            )

            dns_static = self.session.api.path("ip", "dns", "static")

            for record in list(dns_static):
                dns_static.remove(record[".id"])

            return True, "Se ha reseteado la configuración del DNS correctamente."

        except Exception as e:
            return False, f"Error al resetear DNS: {str(e)}"