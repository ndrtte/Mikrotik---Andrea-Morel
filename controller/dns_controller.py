class DnsController:
    def __init__(self, session):
        self.session = session
        
    def get_dns_configuration(self):
        dns_api = self.session.api.path("ip", "dns")
        
        dns_config = list(dns_api)
        
        