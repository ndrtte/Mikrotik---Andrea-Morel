class InterfaceMonitorController:
    def __init__(self, session):
            self.session = session
    
    def get_interface_monitor(self, interface_name):
        try:
            success, info = self.interface_util.get_interface_info(interface_name)

            if not success:
                return False, info

            traffic = self.get_interface_traffic(interface_name)

            name = info.get("name")
            status = "Up" if info.get("running") else "Down"
            rx_traffic = traffic.get("rx")
            tx_traffic = traffic.get("tx")

            interface_data = {
                "name": name,
                "status": status, #Up/Down de interfaz
                "rx": rx_traffic, #Trafico de entrada
                "tx": tx_traffic #Trafico de salida
            }

            return True, interface_data

        except Exception as e:
            return False, str(e)