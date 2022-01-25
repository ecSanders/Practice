#%% Import libraries
import numpy as np
import cv2 as cv
from urllib.request import urlopen

#%% Load image
url = 'https://customers.pyimagesearch.com/wp-content/uploads/2015/06/wynn.png'
request = urlopen(url)
arr = np.asarray(bytearray(request.read()), dtype=np.uint8)
img = cv.imdecode(arr, -1)

#%% Get contours
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#%% Draw contours
all_contour = cv.drawContours(imgray, contours, -1, (0,255,0), 3)
indvdl_contour = cv.drawContours(imgray, contours, 3, (0,255,0), 3)
cnt = contours[4]
best = cv.drawContours(imgray, [cnt], 0, (0,255,0), 1)

#%% Display contoured image
cv.imshow('grayscaled',best)
cv.waitKey(0)
cv.destroyAllWindows()
# %%
