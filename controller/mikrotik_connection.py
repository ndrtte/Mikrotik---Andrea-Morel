from librouteros import connect

class MikroTikService:

    def __init__(self):
        self.api = None

    def connect_router(self, ip, username, password):
        try:
            self.api = connect(
                host=ip,
                username=username,
                password=password
            )

            resource = self.api.path("/system/resource")
            info = list(resource)

            return True, info[0]

        except Exception as e:
            return False, str(e)

    def disconnect(self):
        if self.api:
            self.api.close()