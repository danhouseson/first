print('Initializing...')
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import numpy as np

hello = tf.constant('asdaaaaaaaaaaaaaaasd')
sess = tf.Session()
print(sess.run(hello))