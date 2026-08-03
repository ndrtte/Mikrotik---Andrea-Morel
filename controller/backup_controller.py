from datetime import datetime

class BackupController:
    def __init__(self, session):
         self.session = session
    
    def get_backups(self):
        try:
            files_api = self.session.api.path("/file")
            files = list(files_api)

            backups = []

            for file in files:
                if file.get("type") != "backup":
                    continue

                backups.append({
                    "name": file.get("name"),
                    "size": file.get("size"),
                    "last_modified": file.get("last-modified")
                })

            return backups

        except Exception as e:
            print(f"Error al obtener los backups: {e}")
            return []
        
        
    def create_backup(self, name="", password=""):
        if name.strip() != "":
            backup_name = name.strip()
        else:
            backup_name = f"backup_{datetime.now():%Y-%m-%d_%H-%M-%S}"

        backup_api = self.session.api.path("system", "backup")

        try:
            tuple(
                backup_api(
                    "save",
                    name=backup_name,
                    password=password
                )
            )

            return True, "Backup creado correctamente"

        except Exception as e:
            return False, f"Error al crear el backup: {e}"