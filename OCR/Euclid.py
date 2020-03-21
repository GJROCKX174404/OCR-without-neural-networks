import numpy as np

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