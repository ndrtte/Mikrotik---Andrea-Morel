class RouterSession:

    def __init__(self):
        self.api = None


    def set_connection(self, api):
        self.api = api


    def is_connected(self):
        return self.api is not None
    
    def disconntect(self):
        if self.api:
            self.api.close()
            self.api = None