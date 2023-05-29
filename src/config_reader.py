import json

class ConfigReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def format_json(self):
        try:
            with open(self.file_path) as file:
                data = json.load(file)
                formatted_json = json.dumps(data, indent=4)
                return formatted_json
        except FileNotFoundError:
            return f"Archivo no encontrado: {self.file_path}"
        except json.JSONDecodeError:
            return f"Error al decodificar el archivo JSON: {self.file_path}"
