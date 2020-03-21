# The functions fun1,fun2 and fun3 deals with the calcuations of the shortest path given the distances for all the points.
# This is crucial part of the OCR Algorithm in which the path will be decided for the given image.
import numpy as np
import copy
""" x= np.array([[0,72,84,96,52,44,80,67,58,76],[72,0,62,88,78,73,54,56,72,63],[84,62,0,45,53,68,63,75,59,69],
            [96,88,45,0,69,79,80,48,64,68],[52,78,53,69,0,54,82,79,76,51],[44,73,68,79,54,0,91,82,84,63],
            [80,54,63,80,82,91,0,81,82,84],[67,56,75,48,79,82,81,0,71,78],[58,72,59,64,76,84,82,71,0,64],
            [76,63,69,68,51,63,84,70,64,0]])
y= x
n= 10 """
def fun1(x,i,n):
    l= x
    b= []
    count= 0
    node= i
    for m in range(0,n):
        if(m==0):
            b.append(i)
        k= 9999999
        i= node
        for j in range(0,n):
            if(j in b):  
                continue
            else:
                if(i == j):
                    continue
                if(l[i,j]< k):
                    k= l[i,j]
                    node= j
        if(len(b)!=n):
            b.append(node)
        count=count +k
        #print(b)
    count= count-k
    #print("\n"+str(count))
    b.append(count)
    return(b)


def fun2(x,n):
    a=[]
    for i in range(0,n):
        a.append(fun1(x,i,n))
        #print(a)
    return(a)

def fun3(x,n):

    z=fun2(x,n)
    #print("\n#############     List     ##########\n")
    #print(z)
    e= 9999
    f=[]
    x1= copy.deepcopy(z)
    for i in range(0,n):
        if(z[i][n]<e):
            e= z[i][n]
        
    #print("\n#############     Smallest Path     ##########\n")

    #print("sairam  "+ str(e)+ "\n")
    for i in range(0,n):
        if(x1[i][n] == e):
            f.append(x1[i])
    #print(f)
    #print(z[])

    #print("\nhello i'm in matrix\n")
    return(f)

#fun3(x,n)
