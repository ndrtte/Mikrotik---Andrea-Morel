class InterfaceMonitorController:
    def __init__(self, session, interface_util):
        self.session = session
        self.interface_util = interface_util

    def get_interface_monitor(self, interface_name):
        try:
            success, info = self.interface_util.get_interface_info(interface_name) #es para primero obtener las interfaces disponibles y su informaicion como el nombre y status

            if not success:
                return False, info

            success, traffic = self.get_interface_traffic(interface_name)

            if not success:
                return False, traffic

            name = info.get("name")
            status = "Up" if info.get("running") else "Down"

            #son datos que obtengo de las interfaces monitor-traffic 
            interface_data = {
                "name": name,
                "status": status,
                "rx": traffic.get("rx"), #entrada
                "tx": traffic.get("tx") #salida
            }

            return True, interface_data

        except Exception as e:
            return False, str(e)
    
    def get_interface_traffic(self, interface_name):
        try:
            interface_api = self.session.api.path(
                "interface"
            ) #utilizo la ruta de /interface

            data = list(
                interface_api(
                    "monitor-traffic", #monitor-traffic es por el comando /interface monitor-traffic
                    interface=interface_name,
                    once=True
                )
            )[0]

            return True, {
                "rx": data.get("rx-bits-per-second"), #es para no traer todo el nombre y solo lo entendible
                "tx": data.get("tx-bits-per-second")
            }

        except Exception as e:
            return False, str(e)