import os
import json

class db:
    def __init__(self, name: str):
        self.db_name = name
        self.db_dir = f"data/{name}"

        try:
            os.makedirs(self.db_dir)
        except FileExistsError:
            # Directory already exists, its fine
            pass
    
    def get(self, key: str):
        db_dir = self.db_dir
        
        try:
            file = open(f"{db_dir}/{key}.json", "r")

            data = file.read()

            file.close()

            parsed = json.loads(data)

            return parsed
        except FileNotFoundError:
            return None
        
    def set(self, key: str, data: json):
        db_dir = self.db_dir

        file = open(f"{db_dir}/{key}.json", "w")

        file.write(json.dumps(data))

        file.close()

    def delete(self, key: str):
        db_dir = self.db_dir

        os.remove(f"{db_dir}/{key}.json")