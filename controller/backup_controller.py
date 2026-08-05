from datetime import datetime

class BackupController:
    def __init__(self, session):
         self.session = session
    
    def get_backups(self):
        try:
            files_api = self.session.api.path("/file") #Aca funcione por ejemplo en el mikrotik para ver los files podria poner el /file print 
            files = list(files_api)

            backups = []

            for file in files:
                if file.get("type") != "backup": #Los filtros para solo obtener los files cuyo tipo sea backup
                    continue

                backups.append({#ir añadiendo los backups en un arreglo 
                    "name": file.get("name"),
                    "size": file.get("size"),
                    "last_modified": file.get("last-modified")
                })

            return backups

        except Exception as e:
            print(f"Error al obtener los backups: {e}") #Aca es para indicar cual fue el error en tipo notificacion en pantalla
            return []
        
        
    def create_backup(self, name="", password=""): #Por defecto no es necesario el name ni password entonces los pongo como vacios
        if name.strip() != "": #Si hay nombre sool quito los espacios y asi
            backup_name = name.strip()
        else:
            backup_name = f"backup_{datetime.now():%Y-%m-%d_%H-%M-%S}" #Si no hay nombre, les doy un formato para mantener el orden y con es formato DE YYYY-MM-DD_HH-MM-SS

        backup_api = self.session.api.path("system", "backup") #Aca es por lo mismo de que accedo ahi para crear un backup /system/backup 

        try:
            tuple(
                backup_api(
                    "save", #Esto es porque ejecute save y no algo como add
                    name=backup_name,
                    password=password
                )
            )

            return True, "Backup creado correctamente"

        except Exception as e:
            return False, f"Error al crear el backup: {e}"