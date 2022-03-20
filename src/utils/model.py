import tensorflow as tf


def create_model(loss_function, optimizer, metrics, num_classes, input_shape):
    LAYERS =    [tf.keras.layers.Flatten(input_shape=input_shape, name="inputLayer"),
                tf.keras.layers.Dense(300, activation="relu", name="hiddenLayer1"),
                tf.keras.layers.Dense(100, activation="relu", name="hiddenLayer2"),
                tf.keras.layers.Dense(num_classes, activation="softmax", name="outputLayer")]

    model_clf = tf.keras.models.Sequential(LAYERS)

    model_clf.summary()

    model_clf.compile(loss=loss_function, optimizer=optimizer, metrics=metrics)            
    
    return model_clf  