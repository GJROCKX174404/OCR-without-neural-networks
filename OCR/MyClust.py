import numpy as np
from sklearn.cluster import KMeans

def print_clusters(lm):
    print("\n---------------------Cluster centers---------------------\n")
    print(lm)
    print("\n---------------------------------------------------------\n")

def Get_Clusters(data,num_clusters):
    km = KMeans(n_clusters = num_clusters,n_init = 10,max_iter=300, tol = 1e-04,random_state = 0)   
    km= km.fit(data)
    lm= km.cluster_centers_
    return(lm)

def get_all_points(newim):
    x,x1,x2 = [],[],[]
    for i in range(0,28):
        for j in range(0,28):
            if(newim[i][j] >127):
                x1.append(i)
                x2.append(j)
    x.append(x1)
    x.append(x2) 
    data= np.matrix(x)
    data= np.array(data)
    #print("hello\n")
    data= data.T
    #print(data.shape)
    return(data)

