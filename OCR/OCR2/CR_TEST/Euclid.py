import numpy as np

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