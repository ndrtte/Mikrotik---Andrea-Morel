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
        
        