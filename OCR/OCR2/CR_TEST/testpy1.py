
import numpy as np
import matplotlib.pyplot as graph
import scipy as sp
import math
import mnist
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from scipy.spatial import distance
import copy
import pickle as p

import Hamilton as Ham
import MyClust
#-----
###########       EUCIDIAN-DISTANCES     #############
import Euclid
###########     DESKEWING     ###########
import Deskew
##################################################

train_images= mnist.train_images()
train_labels= mnist.train_labels()
test_images= mnist.test_images()
test_labels= mnist.test_labels()

def newimg(img_no):
    
    newim = Deskew.deskew(test_images[img_no])
    #print(newim)
    data= MyClust.get_all_points(newim)
    #############      CLUSTERING       #################     
    lm= MyClust.Get_Cluster(data,num_clusters)
    lm2=  np.array(Euclid.fun1(lm,num_clusters))
    #print(lm2)   
    lm2= Ham.fun3(lm2,num_clusters)
    lm2= np.array(lm2[0],dtype= np.int64)
    order= lm2[:-1]
    mm= Ham.path_order(order,lm,num_clusters)
    #print(mm)

    return(mm)

def comp(i):
    lbl= []
    mm= []    
    lbl.append(i)
    for i in range(0,len(lbl)):
        xnum= 13
        try:
	        mm1= newimg(lbl[i])     
        except:
            print(lbl[i])
            #print(test_labels[lbl[i]])
        if(xnum < mm1[0,0]):
            mm1= mm1[: :-1]       
        mm.append(mm1.reshape(num_clusters*2,).T)
    #print(mm)
    return(mm)

def cr(dict_range,lrange,hrange):
    count_img=count= 0
    count2= count3 =0
    for img_no in range(lrange,hrange):
        dlist= dlist2 =[]
        listed= comp(img_no)
        count_img+=1
        if count_img % 50 == 0:
            print ("Images processed: " + str(count_img))
        for i in range (10):
            for j in range(dict_range):
                dlist.append(distance.euclidean(listed[0], dict_num[i][j]))
        #dlist.sort()
        #print(dlist)

        dmin= int(dlist.index(min(dlist))/dict_range)
        if(test_labels[img_no] != dmin):
            dlist2=copy.deepcopy(dlist)
            dlist2.sort()       
            dmin2= int(dlist.index(dlist2[1])/dict_range)
            
            if(dmin2 == test_labels[img_no]):
                count2 = count2+1
            dmin3= int(dlist.index(dlist2[2])/dict_range)
            if(dmin3   ==  test_labels[img_no] and dmin != dmin2):
                count3 = count3+1
            
            """ sum=(dlist2[0]+dlist2[1]+dlist2[3])
            print("\nImage Number: ",img_no)
            print("Original Character:",test_labels[img_no])
            print("Recognition probability 1: "+str(dmin)+"\tprobability: "+str(100-(dlist2[0]/sum)*100))
            print("Recognition probability 2: "+str(dmin2)+"\tprobability: "+str(100-(dlist2[1]/sum)*100))
            print("Recognition probability 3: "+str(dmin3)+"\tprobability: "+str(100-(dlist2[2]/sum)*100))
            #print("Character recognised as : ",((dlist2[0]/sum)*100)+(dlist2[1]/sum)*100+(dlist2[2]/sum)*100)
            """
            #print(test_labels[img_no])
            count = count +1
    print("\nUnsuccessfull Count: ",count)
    print("\n2nd successful Count: ",count2)
    print("\n3rd successful Count: ",count3)
    print("\nFor 2&3rd  successful Count: ",count3+count2)
    print("\nAccuracy:", 100 - count/count_img *100)

print("hello")

num_clusters = 15
dict_range= 150
print("Testing with the dictionary range of : ", dict_range)

""" d= {i:comp(i) for i in range(0,10)}
with open('n15.p','wb') as handle:
    p.dump(d,handle) """ 

with open('n15.p','rb') as handle:
    d= p.load(handle)

""" def cl_im(i):
    km1 = KMeans(n_clusters = dict_range,n_init = 10,max_iter=300, tol = 1e-04,random_state = 0)
    km1= km1.fit(d[i])
    hollow1= km1.cluster_centers_
    return(hollow1)

dict_num= {n:cl_im(n) for n in range(0,10)}
#print(dict_num)

#d1= {n:cl_im(n) for n in range(0,10)}

with open('n15d150.p','wb') as handle:
    p.dump(dict_num,handle)  """

with open('n15d600.p','rb') as handle:
    dict_num= p.load(handle)
#print(dict_num)

print("\n\n-----Clusters(like n20d40) are loaded-----\n\n")

lrange,hrange= 0,20

cr(dict_range,lrange,hrange)

print("\n\n--------ENJOY SUCCESSFUL RECOGNISATION  TRY------------\n\n")