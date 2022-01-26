#%% Import libraries
import numpy as np
import cv2 as cv
import pickle

#%% Load image
pkl = open("mrcnn.pickle","rb")
data = pickle.load(pkl)

img = cv.imread('mrcnn_pred.png')

#%%
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (5, 5), 0)
thresh = cv.threshold(blurred, 100, 255, cv.THRESH_BINARY)[1]

#%% 
cv.imshow('mrcnn_pred.png', thresh)
cv.waitKey(0)
cv.destroyAllWindows()
#%%

