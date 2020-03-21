
import numpy as np
import matplotlib.pyplot as graph
import scipy as sp
import math
import mnist
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from scipy.spatial import distance
import copy

import Hamilton as Ham
import MyClust

###########       EUCIDIAN-DISTANCES     #############

import Euclid

###########     DESKEWING     ###########

import Deskew

##################################################


num_clusters = 15

def newimg(img):
    
    newim = Deskew.deskew(img)
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

def comp(lbl):
    mm= []
    
    #print(lbl[0])
    for i in range(0,len(lbl)):

        if i % 100 == 0:
            print("Images loaded : ",str(i))
        #print()
        xnum= 13
        try:
            #print (lbl[i])
            mm1= newimg(lbl[i])         
        except:
            #print(i)
            continue
            #print(test_labels[lbl[i]])
        if(xnum < mm1[0,0]):
            mm1= mm1[: :-1]       
        mm.append(mm1.reshape(num_clusters*2,).T)
    #print(mm)
    print("Images Processed: ",len(lbl))
    return(mm)

def comp2(i):
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


def cr_small(dict_range):
    listed= comp2(d['Y'][42])
    #print(listed[0])
    dlist= dlist2 =[]
    for i in Alphabet_Mapping_List:
        for j in range(dict_range):
            dlist.append(distance.euclidean(listed[0], dict_num[i][j]))
    #print(min(dlist))
    dmin= int(dlist.index(min(dlist))/dict_range)
    #print(dmin)
    print(Alphabet_Mapping_List[dmin])   
    #if('A' == dict_num[])
    #dlist.sort()
        #print(dlist)
def cr_small2(dict_range):
    count_img= count= 0
    count2= count3 =0
    for i in Alphabet_Mapping_List:
        print("\n",i)
        for j in range(len(d[i])):
            count_img+=1
            if count_img % 10 == 0:
                print("No.of Images processed: " + str(count_img))

            listed= comp2(d[i][j])
            dlist= dlist2 =[]
            for k in Alphabet_Mapping_List:
                for l in range(dict_range):
                    dlist.append(distance.euclidean(listed[0], dict_num[k][l]))
            #print(min(dlist))
            dmin= int(dlist.index(min(dlist))/dict_range)

            if( i != Alphabet_Mapping_List[dmin]):
                dlist2=copy.deepcopy(dlist)
                dlist2.sort()

                dmin2= int(dlist.index(dlist2[1])/dict_range)
                dmin3= int(dlist.index(dlist2[2])/dict_range)
                #print(dmin2)
                if(Alphabet_Mapping_List[dmin2] == i):
                    count2= count2+1
                if(Alphabet_Mapping_List[dmin3] == i and i != Alphabet_Mapping_List[dmin2]):
                    count3= count3+1
                count = count +1

                """ sum=(dlist2[0]+dlist2[1]+dlist2[3])
                #print("\nAlphabet Image :  ",Alphabet_Mapping_List[dmin])
                print("Original Character:",i)
                print("Recognition probability 1: "+str(Alphabet_Mapping_List[dmin])+"\tprobability: "+str(100-(dlist2[0]/sum)*100))
                print("Recognition probability 2: "+str(Alphabet_Mapping_List[dmin2])+"\tprobability: "+str(100-(dlist2[1]/sum)*100))
                print("Recognition probability 3: "+str(Alphabet_Mapping_List[dmin3])+"\tprobability: "+str(100-(dlist2[2]/sum)*100))
                #print("Character recognised as : ",((dlist2[0]/sum)*100)+(dlist2[1]/sum)*100+(dlist2[2]/sum)*100)
                 """
            #print(test_labels[img_no])
                
        if( i == 'B'):
            break
    print("\nUnsuccessfull Count: ",count)
    print("\n2nd successful Count: ",count2)
    print("\n3rd successful Count: ",count3)
    print("\nFor 2&3rd  successful Count: ",count3+count2)
    print("\nAccuracy:", 100 - count/count_img *100)
            #print(dmin)
            #print(Alphabet_Mapping_List[dmin])

from PIL import Image
import numpy as np
import matplotlib.image as mpimg
import os
import string
train_images= []

folder = "/home/bca3/Desktop/CR1/CR_KID_VER/Alphabets/Alpha2/alphabet"
#folder = './your/folder/'
if os.path.exists(folder):
    print("sairam")

#l1= l2= []
l3= {}
#print(l1)

Alphabet_Mapping_List = list(string.ascii_uppercase)

import pickle as p
print("hello")
d={}


with open('test500.p','rb') as handle:
    d= p.load(handle)
#print(d['F'][161])
#print(l2[1])

""" 
print("\n\n-----For traiing purpose-----\n\n")

with open('train1000.p','rb') as handle:
    d= p.load(handle)
#print(d['Z'][5000])
#print(l2[1])

print("\n\n-----------------------------\n\n") """



print("\n\n-----Images are loaded-----\n\n")
   
#print(len(d['Z']))
""" d1= {n:comp(d[n]) for n in Alphabet_Mapping_List}
with open('n15file1000.p','wb') as handle:
    p.dump(d1,handle) """
with open('n15file1000.p','rb') as handle:
    d1= p.load(handle)

dict_range= 700

#print(d1)
#print(d1['A'][0])
print("\n\n-----Input is loaded-----\n\n")

print("Testing with dict range: ",dict_range)

def cl_im(i):
    km1 = KMeans(n_clusters = dict_range ,n_init = 10,max_iter=300, tol = 1e-04,random_state = 0)
    km1= km1.fit(i)
    #print(km1)
    hollow1= km1.cluster_centers_
    return(hollow1)
""" dict_num= {n:cl_im(d1[n]) for n in Alphabet_Mapping_List}

with open('n15d700file1000.p','wb') as handle:
    p.dump(dict_num,handle) """ 
with open('n15d700file1000.p','rb') as handle:
    dict_num= p.load(handle)
print("\n\n-----Dict_num(clusters)is loaded-----\n\n")

#print(dict_num['A'])



lrange,hrange= 2,3

#cr(dict_range,lrange,hrange)
cr_small2(dict_range)
#print(d2['A'])
#print(d['A'][0])
#
#print(cl_im(d1['A']))


#print(d1)
#print(comp(d['A']))
#cr(dict_range,lrange,hrange)

print("\n\n--------ENJOY SUCCESSFUL RECOGNISATION  TRY------------\n\n")
import pickle as p
print("hello")