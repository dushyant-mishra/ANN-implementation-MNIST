import yaml


# def read_config(config_file):
#    with open(config_file, "r") as f:
#        config = yaml.load(f, Loader=yaml.FullLoader)
#    return config

def read_config(config_path):
    with open(config_path) as config_file:
        content = yaml.safe_load(config_file)
    return content
