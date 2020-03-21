
import numpy as np
import matplotlib.pyplot as graph
import scipy as sp
import math
import mnist
train_images= mnist.train_images()
train_labels= mnist.train_labels()
test_images= mnist.test_images()
test_labels= mnist.test_labels()

###########     DESKEWING     ###########

from scipy.ndimage import interpolation

def moments(image):
    c0,c1 = np.mgrid[:image.shape[0],:image.shape[1]] # A trick in numPy to create a mesh grid
    totalImage = np.sum(image) #sum of pixels
    m0 = np.sum(c0*image)/totalImage #mu_x
    m1 = np.sum(c1*image)/totalImage #mu_y
    m00 = np.sum((c0-m0)**2*image)/totalImage #var(x)
    m11 = np.sum((c1-m1)**2*image)/totalImage #var(y)
    m01 = np.sum((c0-m0)*(c1-m1)*image)/totalImage #covariance(x,y)
    mu_vector = np.array([m0,m1]) # Notice that these are \mu_x, \mu_y respectively
    covariance_matrix = np.array([[m00,m01],[m01,m11]]) # Do you see a similarity between the covariance matrix
    return mu_vector, covariance_matrix

def deskew(image):
    c,v = moments(image)
    alpha = v[0,1]/v[0,0]
    affine = np.array([[1,0],[alpha,1]])
    ocenter = np.array(image.shape)/2.0
    offset = c-np.dot(affine,ocenter)
    
    return interpolation.affine_transform(image,affine,offset=offset)


img_no = 418
graph.subplot(1, 2, 1)
graph.imshow(255-train_images[img_no], cmap = 'gray')

newim = deskew(train_images[img_no])
graph.subplot(1, 2, 2)
graph.imshow(255-newim, cmap = 'gray')
#print(newim)
graph.show()
x1,x2 = [],[]
for i in range(0,28):
    for j in range(0,28):
        if(newim[i][j] >100):
            x1.append(i)
            x2.append(j)
x= []
x.append(x1)
x.append(x2)
#print(x1)
#print(x2)  
data= np.matrix(x)
data= np.array(data)
print("hello")
data= data.T
#print(data)

x1= np.array(x1)
#print(x1)
x2= np.array(x2)
graph.imshow(255-newim, cmap = 'gray')
graph.scatter(x2,x1,s = 50, c='green',edgecolor= 'black',label = 'cluster')
graph.show()

#############      CLUSTERING       #################

from sklearn.cluster import KMeans
num_clusters = 20
km = KMeans(n_clusters = num_clusters,n_init = 10,max_iter=300, tol = 1e-04,random_state = 0)
km= km.fit(data)
lm= km.cluster_centers_
graph.imshow(255-newim, cmap = 'gray')
graph.plot(km.cluster_centers_[:,1], km.cluster_centers_[:,0], 'c.', MarkerSize = 15)
graph.show()
print("\n---------------------Cluster centers---------------------\n")
print(lm)
print("\n---------------------------------------------------------\n")


###########       EUCIDIAN-DISTANCES     #############


import matrix2 as matrix2
# This function calculates the Euclidian distance between two points
def euclid(x1,y1,x2,y2):
    d= np.sqrt((y2-y1)**2+(x2-x1)**2)
    return(d)
# Finds distance to every point to the other point
def fun(lm,i,n):
    x1,y1,x2,y2= 0,0,0,0
    lm1=[]
    for j in range(0,n):
        x1,y1= lm[i,0],lm[i,1]
        x2,y2= lm[j,0],lm[j,1]
        lm1.append(euclid(x1,y1,x2,y2))
    return(lm1)
# All that lists of distances will be inserted in a single list.
def fun1(lm,n):
    lm2= []
    for i in range(0,n):
        lm2.append(fun(lm,i,n))
    return(lm2)


print("\nSairam bro ")
n= num_clusters
lm2= []
lm2= np.array(fun1(lm,n))
#print(lm2)
list1= matrix2.fun3(lm2,n)
#print(list1)

lbl= []
for i in range(0,100):
    if(train_labels[i] == 1):
        lbl.append(i)
print(lbl)

"""for i in range(0,len(lbl)):
    newim = deskew(train_images[lbl[i]]) """


###########----PLOT-----##########

list2=np.array(list1[0],dtype= np.int64)
order= list2[:-1]

ordered_lm = np.zeros((num_clusters,2)) # intialising ordered_lm with zeroes with shape(num_clusters,2)
j = 0
# loop for getting the ordered list
for i in order:
	ordered_lm[j,:] = lm[int(i),:]
	j = j+1

print("\nShortest path in the order: \n",ordered_lm)
x,y = ordered_lm[:,0],ordered_lm[:,1] # Getting x,y to plot 

graph.imshow(255-newim, cmap = 'gray')
graph.plot(y,x,'wo-',mfc='c',ms= '10')
graph.show()
