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
# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv.findContours(image=thresh, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
# draw contours on the original image
image_copy = img.copy()
cv.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv.LINE_AA)
# see the results
cv.imshow('None approximation', image_copy)
cv.waitKey(0)
cv.imwrite('contours_none_image1.jpg', image_copy)
cv.destroyAllWindows()

# %%
