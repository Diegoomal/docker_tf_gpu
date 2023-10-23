import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf


if __name__ == "__main__":

  print('1) Verifica o acesso a placa de video')
  print(tf.config.list_physical_devices('GPU'))
