########## Import Libraries ###############
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
from tqdm import tqdm
from random import shuffle

import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import ConvLSTM2D,Conv2DTranspose, LayerNormalization, BatchNormalization, TimeDistributed, Conv2D, Flatten, Dense, Dropout
import keras
import pprint

########### TPU conversion ################
### Remove the comments of these lines if you want to train the model on TPU

# if 'COLAB_TPU_ADDR' not in os.environ:
#   print('ERROR: Not connected to a TPU runtime; please see the first cell in this notebook for instructions!')
# else:
#   tpu_address = 'grpc://' + os.environ['COLAB_TPU_ADDR']
#   print ('TPU address is', tpu_address)

#   with tf.compat.v1.Session(tpu_address) as session:
#     devices = session.list_devices()
    
#   print('TPU devices:')
#   pprint.pprint(devices)

# resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='grpc://' + os.environ['COLAB_TPU_ADDR'])
# tf.config.experimental_connect_to_cluster(resolver)
# # This is the TPU initialization code that has to be at the beginning.
# tf.tpu.experimental.initialize_tpu_system(resolver)
# print("All devices: ", tf.config.list_logical_devices('TPU'))
# strategy = tf.distribute.TPUStrategy(resolver)


############### Variable initialization ##############

class Config():
	'''
	Docstring : This class will initialize all the parameters we need for model training.
	'''
	def __init__(self, train_path, test_path, model_path, train_anom, img_size = (128, 128), batch_size = 3, mx_frm = 4000, stride = [1,2], frm_cnt = 20, test_size = 400, epochs = 10):
	    self.train_path = train_path
	    self.test_path = test_path
	    self.img_size = img_size
	    self.batch_size = batch_size
	    self.model_path = model_path
	    self.train_anom = train_anom
	    self.epochs = epochs
	    self.stride = stride
	    self.mx_frm = mx_frm
	    self.frm_cnt = frm_cnt
	    self.test_size = test_size