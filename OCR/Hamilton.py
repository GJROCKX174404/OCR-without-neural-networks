import numpy as np
import copy

# The functions fun1,fun2 and Shortest_path_way deals with the calcuations of the shortest path given the distances for all the points.
# This is crucial part of the OCR Algorithm in which the path will be decided for the given image.

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

def Shortest_path_way(x,n):
    z=fun2(x,n)
    #print("\n#############     List     ##########\n")
    #print(z)
    e= 9999
    x1= copy.deepcopy(z)
    for i in range(0,n):
        if(z[i][n]<e):
            e= z[i][n]        
    #print("\n#############     Smallest Path     ##########\n")
    #print("sairam  "+ str(e)+ "\n")
    f=[]
    for i in range(0,n):
        if(x1[i][n] == e):
            f.append(x1[i])
    #print(f)
    #print(z[])
    #print("\nhello i'm in matrix\n")
    return(f)
#fun3(x,n)

# This function gives the shortest path and arranging the clustercenters(lm) in the order of the shortest path.
def path_order(order,lm,num_clusters):
    ordered_lm = np.zeros((num_clusters,2))  # intialising ordered_lm with zeroes with shape(num_clusters,2)
    j = 0
    for i in order:  # This loop gives the ordered list of cluster list
	    ordered_lm[j,:] = lm[int(i),:]
	    j = j+1
    #print(ordered_lm)
    return(ordered_lm)
    