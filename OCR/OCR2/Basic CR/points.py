
import numpy as np
import matplotlib.pyplot as graph
import scipy as sp
import math
import mnist
from sklearn.cluster import KMeans
import matrix2 as matrix2

train_images= mnist.train_images()
train_labels= mnist.train_labels()
test_images= mnist.test_images()
test_labels= mnist.test_labels()

###########       EUCIDIAN-DISTANCES     #############

def euclid(x1,y1,x2,y2):
    d= np.sqrt((y2-y1)**2+(x2-x1)**2)
    return(d)

def fun(lm,i,n):
    x1,y1,x2,y2= 0,0,0,0
    lm1=[]
    for j in range(0,n):
        x1,y1= lm[i,0],lm[i,1]
        x2,y2= lm[j,0],lm[j,1]
        lm1.append(euclid(x1,y1,x2,y2))
    return(lm1)

def fun1(lm,n):
    lm2= []
    for i in range(0,n):
        lm2.append(fun(lm,i,n))
    return(lm2)

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


#############-----ORDER-----#########


def lms(order,lm):
    ordered_lm = np.zeros((num_clusters,2))
    j = 0
    for i in order:
	    ordered_lm[j,:] = lm[int(i),:]
	    j = j+1
    #print(ordered_lm)
    """ x,y = ordered_lm[:,0],ordered_lm[:,1]
    fp= []
    fp.append(list(ordered_lm[0]))
    fp.append(list(ordered_lm[-1])) """
    #print(fp)
    return(ordered_lm)

##################################################


num_clusters = 20


def newimg(img_no):
    x1,x2 = [],[]
    newim = deskew(train_images[img_no])

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
    #print("hello\n")
    data= data.T


    #############      CLUSTERING       #################

    km = KMeans(n_clusters = num_clusters,n_init = 10,max_iter=300, tol = 1e-04,random_state = 0)
    km= km.fit(data)
    lm= km.cluster_centers_
    
    #print("\n---------------------Cluster centers---------------------\n")
    #print(lm)
    #print("\n---------------------------------------------------------\n")
    n= num_clusters
    lm2= []
    lm2= np.array(fun1(lm,n))
    #print(lm2)
    list1= matrix2.fun3(lm2,n)
    #print(list1)

    list2=np.array(list1[0],dtype= np.int64)
    order= list2[:-1]
    mm= lms(order,lm)
    return(mm)

def comp(n):
    lbl= []
    mm= []
    num= n
    
    for i in range(0,500):
        if(train_labels[i] == num):
            lbl.append(i)

    #print("Number: "+str(num)+"\n"+str(lbl))

    for i in range(0,len(lbl)):
        xnum= 13
        #l = list()
        #print("\n"+str(lbl[i]))
        try:
	        mm1= newimg(lbl[i])
            
        except:
            #continue
            print(lbl[i])
        #mm1= newimg(lbl[i])
        if(xnum < mm1[0,0]):
            #xnum= int(mm1[-1,-2]) - 5
            mm1= mm1[: :-1]
        mm.append(mm1.reshape(22,).T)
        
    return(mm)

listed= [] 
n=0

d= {i:comp(i) for i in range(0,10)}

import pickle as p
with open('myfile.p','wb') as handle:
    p.dump(d,handle) 
with open('myfile.p','rb') as handle:
    d= p.load(handle)

#print(d[0])

def cl_im(i):
    km1 = KMeans(n_clusters = 1,n_init = 10,max_iter=300, tol = 1e-04,random_state = 0)
    km1= km1.fit(d[i])
    hollow1= km1.cluster_centers_
    return(hollow1)


d1= {n:cl_im(n) for n in range(0,10)}

with open('myfile1.p','wb') as handle:
    p.dump(d1,handle) 
with open('myfile1.p','rb') as handle:
    d1= p.load(handle)
print("\n\n-----Centroids are loaded-----\n\n")
#print(d1)

#listed= np.array(listed)
#print("CHECKING : ")
#print(listed.shape)
#print(listed)
#print(listed[0][0])
print("\n######-----LISTED------######\n")
#print(d[1][0])

#print(listed)
#d={0:{0:listed[0],1:listed[1]}}
""" n=0
d= {2:listed}
#d= {n:{n:listed[n] for n in range(0,len(listed))}}
#d= {x for sublist in listoflists for x in listed}
#print(d[0][1]) 
import pickle as p
with open('myfile.p','wb') as handle:
    p.dump(d,handle) 
with open('myfile.p','rb') as handle:
    d= p.load(handle)
#print(d[3][1])
km1 = KMeans(n_clusters = 1,n_init = 10,max_iter=300, tol = 1e-04,random_state = 0)
km1= km1.fit(listed)
hollow1= km1.cluster_centers_
print("sairam")
print(hollow1) """









