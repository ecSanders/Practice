#%% Import libraries
import numpy as np
import cv2 as cv
import pickle as pickle # Hahaha

#%% Unpickle and load image
pkl = open("mrcnn.pickle","rb")
data = pickle.load(pkl)

img = cv.imread('mrcnn_pred.png')
#%% Display image
cv.imshow('mrcnn_pred.png', img)
cv.waitKey(0)
cv.destroyAllWindows()
# %% 
