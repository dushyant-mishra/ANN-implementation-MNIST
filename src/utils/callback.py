import tensorflow as tf
import os
import numpy as np
import time
from utils.common import get_timestamp

def get_callbacks(config, X_train):
    logs = config['logs']
    unique_dir_name = get_timestamp("tb_logs")
    tensorboard_root_log_dir = os.path.join(logs["logs_dir"],logs["tensorboard_root_log_dir"], unique_dir_name)
    
    os.makedirs(tensorboard_root_log_dir, exist_ok=True)
   
    tensorboard_cb = tf.keras.callbacks.TensorBoard(log_dir=tensorboard_root_log_dir)

    file_writer = tf.summary.create_file_writer(logdir= tensorboard_root_log_dir)

    with file_writer.as_default():
        images = np.reshape(X_train[10:30], (-1, 28,28,1))
        tf.summary.image("20 handwritten digit samples", images, max_outputs = 25, step = 0)   

    params = config["params"]
    early_stopping_cb = tf.keras.callbacks.EarlyStopping(
        patience=params["patience"], 
        restore_best_weights=params["restore_best_weights"])
    
    artifacts = config["artifacts"]
    ckpt_dir = os.path.join(artifacts["artifacts_dir"], artifacts["checkpoint_dir"])
    os.makedirs(ckpt_dir, exist_ok=True)
    
    ckpt_path = os.path.join(ckpt_dir, "model_ckpt.h5")

    checkpointing_cb = tf.keras.callbacks.ModelCheckpoint(ckpt_path, save_best_only=params["save_best_only"])

    return[tensorboard_cb, checkpointing_cb, early_stopping_cb]   

    