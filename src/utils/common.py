import yaml
import time


def read_config(config_path):
    with open(config_path) as config_file:
        content = yaml.safe_load(config_file)

    return content

# def read_config(config_file):
#    with open(config_file, "r") as f:
#        config = yaml.load(f, Loader=yaml.FullLoader)
#    return config


def get_timestamp(name):       #implemented differently using asctime than the get_unique_filename function in utils/model.py
    timestamp = time.asctime().replace(" ", "_").replace(":", "_")
    unique_name =  f"{name}_at_{timestamp}"
    return unique_name