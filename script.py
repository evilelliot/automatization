from src.config_reader import ConfigReader

file_path = "./config/config.json"
config_reader = ConfigReader(file_path)
config_reader.print_formatted_json()