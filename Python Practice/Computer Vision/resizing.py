#%% 
import numpy as np
import cv2 as cv
from urllib.request import urlopen

#%% Load image
url = 'https://customers.pyimagesearch.com/wp-content/uploads/2015/06/wynn.png'

req = urlopen(url)
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv.imdecode(arr, -1)

#%% Display image
cv.imshow('test', img)
cv.waitKey(0)
cv.destroyAllWindows()
# %% Aspect ratio
w,h = img.shape[:2]
ratio = w/h

# %%
