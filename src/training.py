from utils.common import read_config
from utils.data_mgmt import get_data
from utils.model import create_model, save_model
import os
import argparse


def training(config_path):
    config = read_config(config_path)
    validation_datasize = config["params"]["validation_datasize"]
    get_data(validation_datasize)
    (X_train, y_train), (X_valid, y_valid), (X_test, y_test) = get_data(validation_datasize)

    loss_function = config["params"]["loss_function"]
    optimizer = config["params"]["optimizer"]
    metrics = config["params"]["metrics"]
    num_classes = config["params"]["num_classes"]
    input_shape = config["params"]["input_shape"]

    model = create_model(loss_function, optimizer, metrics, num_classes, input_shape)

    epochs = config["params"]["epochs"]
    validation = (X_valid, y_valid)

    history = model.fit(X_train, y_train, epochs=epochs, validation_data=validation)

    artifacts_dir = config["artifacts"]["artifacts_dir"]
    model_dir = config["artifacts"]["model_dir"]

    model_dir_path = os.path.join(artifacts_dir, model_dir)
    os.makedirs(model_dir_path, exist_ok=True)

    model_name = config["artifacts"]["model_name"]

    save_model(model, model_name, model_dir_path)


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config.yaml")

    parsed_args = args.parse_args()

    training(config_path=parsed_args.config)
