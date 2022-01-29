'''
Author: Erik Sanders
Company: Design for Making
Date: 1/27/2022
Status: Benched (Taking a new approach)

Description: 
Determine the orientation of an object in an image.
'''


#%% Import libraries
import numpy as np
import cv2 as cv
import pickle as pickle # Hahaha

#%% Unpickle and load image
pkl = open("data/mrcnn01.pickle","rb")
data = pickle.load(pkl)['masks']
data = data.astype(int)
# data = np.pad(data,((0,0),(0,0),(0,1)), mode='edge')

img = cv.imread('images/mrcnn_pred01.png')

#%% Scale image (too big) and display
scale_percent = 80
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

# Blur 
img_blur = cv.GaussianBlur(imgray, (1,1), 0) 
cv.imshow('T-gray',imgray)
cv.waitKey(0)
cv.imshow('T-gray/blur',img_blur)
cv.waitKey(0)
cv.destroyAllWindows()

#%% Run Canny edge detection
canny = cv.Canny(img_blur,90,110)
cv.imshow('T-canny', canny)
cv.waitKey(0)
cv.destroyAllWindows()

# %% Get contours
ret, thresh = cv.threshold(canny, 100, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
disp = scaled.copy()
cv.drawContours(disp, contours, -1, (0,255,0), 1, cv.LINE_AA)

cv.imshow('T - edge/blur', disp)
cv.waitKey(0)
cv.imshow('T - scaled', scaled)
cv.waitKey(0)
cv.destroyAllWindows()

# %% Apply hull
# create hull array for convex hull points
hull = []

# calculate points for each contour
for ele in contours:
    # creating convex hull object for each contour
    print(ele)
    hull.append(cv.convexHull(ele, False))

# create an empty black image
drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

# draw contours and hull points
for i in range(len(contours)):
    # color_contours = (0, 255, 0) # green - color for contours
    color = (255, 0, 0) # blue - color for convex hull
    # draw ith contour
    # cv.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
    # draw ith convex hull object
    cv.drawContours(drawing, hull, i, color, 1, 8)

cv.imshow('T - hull', drawing)
cv.waitKey(0)
cv.destroyAllWindows()
# %%
