#%% Import libraries
import cv2 as cv
import numpy as np
from urllib.request import urlopen

#%% Load image
url = 'https://customers.pyimagesearch.com/wp-content/uploads/2015/06/wynn.png'
request = urlopen(url)
arr = np.asarray(bytearray(request.read()), dtype=np.uint8)
img = cv.imdecode(arr, -1)

# %% Get data
w,h = img.shape[:2]
Cx, Cy = w//2, h//2

#%% Rotate
M = cv.getRotationMatrix2D((50,50),88,1)
R = cv.warpAffine(img,M,(w,h))

#%% Display
cv.imshow('quiz 01', R)
cv.waitKey(0)
cv.destroyAllWindows()

# %% Solution
b,g,r = R[10,10]
print(r,g,b)
# %%
