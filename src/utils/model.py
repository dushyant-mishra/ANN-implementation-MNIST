import time
import os

import tensorflow as tf


def create_model(loss_function, optimizer, metrics, num_classes, input_shape):
    layers = [tf.keras.layers.Flatten(input_shape=input_shape, name="inputLayer"),
              tf.keras.layers.Dense(300, activation="relu", name="hiddenLayer1"),
              tf.keras.layers.Dense(100, activation="relu", name="hiddenLayer2"),
              tf.keras.layers.Dense(num_classes, activation="softmax", name="outputLayer")]

    model_clf = tf.keras.models.Sequential(layers)

    model_clf.summary()

    model_clf.compile(loss=loss_function, optimizer=optimizer, metrics=metrics)

    return model_clf


def get_unique_filename(filename):
    unique_filename = time.strftime(f"%Y%m%d-%H%M%S_{filename}")
    return unique_filename


def save_model(model, model_name, model_dir):
    unique_filename = get_unique_filename(model_name)
    path_to_model = os.path.join(model_dir, unique_filename)
    model.save(path_to_model)
