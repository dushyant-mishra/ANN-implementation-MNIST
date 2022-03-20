from src.utils.common import read_config
from src.utils.data_mgmt import get_data
import argparse

def training(config_path):
    config = read_config(config_path)
    validation_datasize = config["params"]["validation_datasize"]
    get_data(validation_datasize)
    (X_train, y_train), (X_val, y_val), (X_test, y_test) = get_data(validation_datasize)    


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config.yaml", help="path to config file")

    parsed_args = args.parse_args()
    
    training(config_path=parsed_args.config)