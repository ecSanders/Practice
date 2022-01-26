#%% Import libraries
import numpy as np
import cv2 as cv
import pickle as pickle # Hahaha

#%% Unpickle and load image
pkl = open("mrcnn.pickle","rb")
data = pickle.load(pkl)

img = cv.imread('mrcnn_pred.png')
#%% Display image
# cv.imshow('mrcnn_pred.png', img)
# cv.waitKey(0)
# cv.destroyAllWindows()
# %% Get contours
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 145, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#%% Draw contours
cnt = contours[4]
cv.drawContours(img, contours, -1, (0,255,0), 2)

#%% 
cv.imshow('mrcnn_pred.png', img)
cv.waitKey(0)
cv.destroyAllWindows()


# %% Find perfect contour


# %%
