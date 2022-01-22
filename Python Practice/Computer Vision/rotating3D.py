#%%
import cv2 as cv
import math as m
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from urllib.request import urlopen
#%% Let's setup an image
url = 'https://www.mcall.com/resizer/s3YcArprk4yxuJHrnbhlCbXK3ws=/800x450/top/cloudfront-us-east-1.images.arcpublishing.com/tronc/4SHUTDKWUJBQXALP7LBBUUGSXM.jpg'

request = urlopen(url)
arr = np.asarray(bytearray(request.read()), dtype=np.uint8)
img = cv.imdecode(arr, -1)

#%% Grab some imformation
roi = [127, 372, 321, 455]
depth = 3 # We'll just assign one
h,w,channel = img.shape

#%% Take a look at our bbox/roi
img[127,:] = [255,0,0]
img[372,:] = [255,0,0]
img[:,321] = [255,0,0]
img[:,455] = [255,0,0]

# Key:
# Look at our "x" and "y"
img[0,:] = [0,0,255] # Red:x:width
img[:,0] = [0,255,0] # Green:y:height
cv.imshow('test', img) 
cv.waitKey(0)
cv.destroyAllWindows()

#%% Reset image  
url = 'https://www.mcall.com/resizer/s3YcArprk4yxuJHrnbhlCbXK3ws=/800x450/top/cloudfront-us-east-1.images.arcpublishing.com/tronc/4SHUTDKWUJBQXALP7LBBUUGSXM.jpg'

request = urlopen(url)
arr = np.asarray(bytearray(request.read()), dtype=np.uint8)
img = cv.imdecode(arr, -1)

#%%
# Angle
theta = 45

# Corners of cube
xdata = np.array([1,1,1,1,3,3,3,3])
ydata = np.array([1,1,3,3,1,1,3,3])
zdata = np.array([1,3,1,3,1,3,1,3])

# Matrix
A = np.array([xdata,
              ydata,
              zdata])
#3D Rotation
R = np.array([[m.cos(theta), -m.sin(theta),0],
              [m.sin(theta), m.cos(theta),0],
             [0,0,1]])

# Apply rotation
Q = R@A 

xdata = Q[0,:]
ydata = Q[1,:]
zdata = Q[2,:]

# Look into
# Rotatate about an axis (non x,y,z)
# Gimble lock
# Quarternians

#%%
ax = plt.axes(projection='3d')
ax.scatter3D(xdata, ydata, zdata);
# %%
