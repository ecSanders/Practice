'''
Author: Erik Sanders
Company: Self
Date: 1/27/2022
Status: Complete

Description:
This was a tutorial that I followed to learn more about contour in the 
context of object detection. Here is the link you are interested:

https://learnopencv.com/contour-detection-using-opencv-python-c/
'''









################################
#           SETUP              #
################################

#%% Import libraries
import numpy as np
import cv2 as cv

#%% Load image and display image
img = cv.imread('images/hot_knife.jpg')
cv.imshow('T - original', img)
cv.waitKey(0)
cv.destroyAllWindows()

#%% Scale image (too big)
percent_scale = 100
width = int(img.shape[1] * percent_scale / 100)
height = int(img.shape[0] * percent_scale / 100)
dim = (width, height)

scaled = cv.resize(img, dim, interpolation=cv.INTER_AREA)

cv.imshow('T - Scaled', scaled)
cv.waitKey(0)
cv.destroyAllWindows()


















##################################
#        CONTOUR COLOR           #
##################################

#%% Split colors 
b,g,r = cv.split(scaled)

cv.imshow('T - blue(all)', b)
cv.waitKey(0)
cv.destroyAllWindows()

#%% Blue contour
blue_cont, b_hierarchy = cv.findContours(b, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
blue = scaled.copy()
cv.drawContours(blue, blue_cont, -1, (0, 255, 0), 2, lineType=cv.LINE_AA)

# Display

cv.imshow('T - blue(contoured)', blue)
cv.waitKey(0)
cv.destroyAllWindows()

#%% Green Contour
green_cont, g_hierarchy = cv.findContours(g,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
green = scaled.copy()
cv.drawContours(green, green_cont, -1, (0,255,0), 2, lineType=cv.LINE_AA)

# Display

cv.imshow('T - green(contoured)', green)
cv.waitKey(0)
cv.destroyAllWindows()


#%% Red contour
red_cont, r_hierarchy = cv.findContours(r,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
red = scaled.copy()
cv.drawContours(red, red_cont, -1, (0,255,0), 2, lineType=cv.LINE_AA)

# Display
cv.imshow('T - red(contoured)', red)
cv.waitKey(0)
cv.destroyAllWindows()











##################################
#     CONTOUR -(SIMPLE/NONE)     #
##################################

#%% CHAIN_APPROX_SIMPLE
img_simple = scaled.copy()
imgray = cv.cvtColor(img_simple, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 150, 255, cv.THRESH_BINARY)
binary_cont, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img_simple, binary_cont, -1, (0,255,0), 2, cv.LINE_AA)

cv.imshow('T - SIMPLE',img_simple)
cv.waitKey(0)
cv.destroyAllWindows()

#%% CHAIN_APPROX_NONE
img_none = scaled.copy()
imgray = cv.cvtColor(img_none, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 150, 255, cv.THRESH_BINARY)
binary_cont, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img_none, binary_cont, -1, (0,255,0), 2, cv.LINE_AA)

cv.imshow('T - NONE',img_none)
cv.waitKey(0)
cv.destroyAllWindows()














#############################
#    HIERARCHY RETRIEVAL    #
#############################

#%% RETR_LIST
list_img = scaled.copy()
imgray = cv.cvtColor(list_img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 150, 255, cv.THRESH_BINARY)
list_cont, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
cv.drawContours(list_img, list_cont, -1, (0,255,0), 2, cv.LINE_AA)

cv.imshow('T - LIST', list_img)
cv.waitKey(0)
cv.destroyAllWindows()

#%% RETR_EXTERNAL 
external_img = scaled.copy()
imgray = cv.cvtColor(external_img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 150, 255, cv.THRESH_BINARY)
external_cont, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
cv.drawContours(external_img, external_cont, -1, (0,255,0), 2, cv.LINE_AA)

cv.imshow('T - EXTERNAL', external_img)
cv.waitKey(0)
cv.destroyAllWindows()

#%% RETR_CCOMP
ccomp_img = scaled.copy()
imgray = cv.cvtColor(ccomp_img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 150, 255, cv.THRESH_BINARY)
ccomp_cont, hierarchy = cv.findContours(thresh, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
cv.drawContours(ccomp_img, ccomp_cont, -1, (0,255,0), 2, cv.LINE_AA)

cv.imshow('T - CCOMP', ccomp_img)
cv.waitKey(0)
cv.destroyAllWindows()

#%% RETR_TREE
tree_img = scaled.copy()
imgray = cv.cvtColor(tree_img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 150, 255, cv.THRESH_BINARY)
tree_cont, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
cv.drawContours(tree_img, tree_cont, -1, (0,255,0), 2, cv.LINE_AA)

cv.imshow('T - TREE', tree_img)
cv.waitKey(0)
cv.destroyAllWindows()
# %%



#########################
#       EXTRA           #
#########################

# #%% Run Sobel edge detection
# sobelx = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
# sobely = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
# sobelxy = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection

# # Display Sobel Edge Detection Images
# cv.imshow('Sobel X', sobelx)
# cv.waitKey(0)
# cv.imshow('Sobel Y', sobely)
# cv.waitKey(0)
# cv.imshow('Sobel X Y using Sobel() function', sobelxy)
# cv.waitKey(0)
# cv.destroyAllWindows()


# #%% Sharpen
# kernel = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])
# im = cv.filter2D(imgray, -1, kernel)

# cv.imshow('T - sharpened', im)
# cv.waitKey(0)
# cv.destroyAllWindows()
# %%
 