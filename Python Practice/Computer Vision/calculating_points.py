#%% Import libraries
import numpy as np
import cv2 as cv
import pickle as pickle # Hahaha

#%% Unpickle and load image
pkl = open("mrcnn.pickle","rb")
mrcnn_info = pickle.load(pkl)