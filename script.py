from src.config_reader import ConfigReader

file_path = "./config/config.json"
config_reader = ConfigReader(file_path)
formatted_json = config_reader.format_json()
print(formatted_json)
