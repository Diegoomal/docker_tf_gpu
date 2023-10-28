# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import time
import tensorflow as tf


if __name__ == "__main__":

  print('1) Verify GPU access')
  print(tf.config.list_physical_devices('GPU'))

  def test(proc_env):
    
    start_time_cpu = time.time()
    
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
    c = tf.matmul(a, b)
    
    print(c)
    
    delta_time = time.time() - start_time_cpu
    print(f'execution time {proc_env}: {delta_time} seconds')

  with tf.device('/cpu:0'):
    test('cpu')

  with tf.device('/gpu:0'):
    test('gpu')
