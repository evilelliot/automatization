import argparse
from src.config_reader import ConfigReader

# Crear el analizador de argumentos
parser = argparse.ArgumentParser(description='Script de configuración')
parser.add_argument('-f', '--file', type=str, help='Ruta al archivo de configuración')

# Obtener los argumentos de la línea de comandos
args = parser.parse_args()

# Verificar si se proporcionó un archivo de configuración
if args.file:
    file_path = args.file
else:
    raise ValueError("Debe proporcionar la ruta al archivo de configuración utilizando el argumento -f/--file")

# Crear una instancia de ConfigReader y procesar el archivo de configuración
config_reader = ConfigReader(file_path)
config_reader.print_formatted_json()
