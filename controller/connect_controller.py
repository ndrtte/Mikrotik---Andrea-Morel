from librouteros import connect

class ConnectController:
    def __init__(self, session):
        self.session = session

    def connect_router(self, ip, username, password):
        try:
            api = connect(
                host=ip,
                username=username,
                password=password
            )

            self.session.set_connection(api)

            resource = api.path("/system/resource")
            info = list(resource)

            return True, info[0]

        except Exception as e:
            return False, str(e)
