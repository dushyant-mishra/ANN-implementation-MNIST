from src.utils.common import read_config
from src.utils.data_mgmt import get_data
from src.utils.model import create_model
import argparse

def training(config_path):
    config = read_config(config_path)
    validation_datasize = config["params"]["validation_datasize"]
    get_data(validation_datasize)
    (X_train, y_train), (X_valid, y_valid), (X_test, y_test) = get_data(validation_datasize)
    
    loss_function= config["params"]["loss_function"]
    optimizer= config["params"]["optimizer"]
    metrics= config["params"]["metrics"]
    num_classes= config["params"]["num_classes"]
    input_shape= config["params"]["input_shape"]


    model_clf = create_model(loss_function, optimizer, metrics, num_classes, input_shape)

    EPOCHS = config["params"]["epochs"]
    VALIDATION = (X_valid, y_valid) 

    history = model_clf.fit(X_train, y_train, epochs=EPOCHS, validation_data=VALIDATION)    


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config.yaml", help="path to config file")

    parsed_args = args.parse_args()
    
    training(config_path=parsed_args.config)