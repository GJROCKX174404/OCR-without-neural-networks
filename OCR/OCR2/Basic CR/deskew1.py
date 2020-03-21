# Deskewing

# When we write, we often write at angles to the paper, which cause letters and numbers to be skewed.
# Unfortunately, unlike the human eye, computers cannot easily find similarities between images that are transformations of each other.
# Thus, the process of deskewing helps in recognition.

#Very formally, deskewing is the process of straightening an image that has been scanned or written crookedly — that is an image that is slanting too far in one direction, or one that is misaligned.

# This is the code which is taken from the internet.
## Default imports: don't touch these

import numpy as np
import matplotlib.pyplot as graph
import scipy as sp
import math
import mnist
train_images= mnist.train_images()
train_labels= mnist.train_labels()
test_images= mnist.test_images()
test_labels= mnist.test_labels()
#train_images= 255-train_images

from scipy.ndimage import interpolation

def moments(image):
    c0,c1 = np.mgrid[:image.shape[0],:image.shape[1]] # A trick in numPy to create a mesh grid
    print(np.mgrid[:image.shape[0],:image.shape[1]])
    totalImage = np.sum(image) #sum of pixels
    print(np.sum(image))
    m0 = np.sum(c0*image)/totalImage #mu_x
    m1 = np.sum(c1*image)/totalImage #mu_y
    m00 = np.sum((c0-m0)**2*image)/totalImage #var(x)
    m11 = np.sum((c1-m1)**2*image)/totalImage #var(y)
    m01 = np.sum((c0-m0)*(c1-m1)*image)/totalImage #covariance(x,y)
    mu_vector = np.array([m0,m1]) # Notice that these are \mu_x, \mu_y respectively
    covariance_matrix = np.array([[m00,m01],[m01,m11]]) # Do you see a similarity between the covariance matrix
    print(np.array([[m00,m01],[m01,m11]]))
    return mu_vector, covariance_matrix

def deskew(image):
    c,v = moments(image)
    alpha = v[0,1]/v[0,0]
    affine = np.array([[1,0],[alpha,1]])
    ocenter = np.array(image.shape)/2.0
    offset = c-np.dot(affine,ocenter)
    return interpolation.affine_transform(image,affine,offset=offset)




