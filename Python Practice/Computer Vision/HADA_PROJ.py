'''
Author: Erik Sanders
Company: Design for Making
Status: In progress (learning)
'''


#%% Import libraries
import numpy as np
import cv2 as cv
import pickle as pickle # Hahaha

#%% Unpickle and load image
pkl = open("data/mrcnn.pickle","rb")
data = pickle.load(pkl)

img = cv.imread('images/parallel.jpg')

#%% Scale image (too big)
scale_percent = 30 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)

#%% Check img scaling
cv.imshow('T-scaled',resized)
cv.waitKey(0)
cv.destroyAllWindows()
# %% Get contours
imgray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 145, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#%% Draw contours
cnt = contours[4]
cv.drawContours(resized, contours, -1, (0,255,0), 2)

#%% 
cv.imshow('mrcnn_pred.png', resized)
cv.waitKey(0)
cv.destroyAllWindows()


# %% Find perfect contour


# %%
