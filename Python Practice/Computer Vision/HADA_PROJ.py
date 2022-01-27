'''
Author: Erik Sanders
Company: Design for Making
Date: 1/27/2022
Status: In progress

Description: 
Determine the orientation of an object in an image.
'''


#%% Import libraries
import numpy as np
import cv2 as cv
import pickle as pickle # Hahaha

#%% Unpickle and load image
pkl = open("data/mrcnn.pickle","rb")
data = pickle.load(pkl)

img = cv.imread('images/T.jpg')

#%% Scale image (too big) and display
scale_percent = 30
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

scaled = cv.resize(img, dim, interpolation = cv.INTER_AREA)

# display
cv.imshow('T-scaled',scaled)
cv.waitKey(0)
cv.destroyAllWindows()

#%% Preprocess image
imgray = cv.cvtColor(scaled, cv.COLOR_BGR2GRAY)

cv.imshow('T-gray',imgray)
cv.waitKey(0)
cv.destroyAllWindows()

img_blur = cv.GaussianBlur(imgray, (9,9), 0) 
cv.imshow('T-gray/blur',img_blur)
cv.waitKey(0)
cv.destroyAllWindows()

#%% Run Sobel edge detection
sobelx = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection

# Display Sobel Edge Detection Images
cv.imshow('Sobel X', sobelx)
cv.waitKey(0)
cv.imshow('Sobel Y', sobely)
cv.waitKey(0)
cv.imshow('Sobel X Y using Sobel() function', sobelxy)
cv.waitKey(0)
cv.destroyAllWindows()
# %% Get contours
ret, thresh = cv.threshold(imgray, 100, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)


# %%
