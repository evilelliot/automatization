import json
from colorama import Fore, Style


class ConfigReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def format_json(self, data, indent_level=0):
        formatted_output = ""
        indent = "  " * indent_level
        for key, value in data.items():
            formatted_output += f"{indent}{Fore.GREEN}{key}:{Style.RESET_ALL} "
            if isinstance(value, dict):
                formatted_output += "\n" + self.format_json(value, indent_level + 1)
            elif isinstance(value, list):
                formatted_output += "[\n"
                for item in value:
                    if isinstance(item, dict):
                        formatted_output += self.format_json(item, indent_level + 2)
                    else:
                        formatted_output += f"{indent}  {item}\n"
                formatted_output += f"{indent}]\n"
            else:
                formatted_output += f"{value}\n"
        return formatted_output

    def print_formatted_json(self):
        try:
            with open(self.file_path) as file:
                data = json.load(file)
                formatted_json = self.format_json(data)
                print(formatted_json)
        except FileNotFoundError:
            print(f"Archivo no encontrado: {self.file_path}")
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo JSON: {self.file_path}")


