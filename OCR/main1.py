#import mnist
import os
import math
import copy
import string
import pickle as p
import numpy as np
import matplotlib.pyplot as graph
import matplotlib.image as mpimg
import scipy as sp
from scipy.spatial.distance import cdist
from scipy.spatial import distance
from sklearn.cluster import KMeans
from PIL import Image
###########      MY LIBRARIES #########
import MyClust              #MyClust
import Euclid               #EUCIDIAN-DISTANCES
import Deskew               #DESKEWING
import Hamilton as Ham      #Shortest path with less cost
##################################################

num_clusters = 15
crrange=0
dict_range= 700
num_range= 600

def newimg(img):                                                #Image will be taken for Deskewing
    newim = Deskew.deskew(img)                                  #Deskew the image
    #print(newim)
    data= MyClust.get_all_points(newim)                         #Gives all points according to threshold
    print("Shape:",data.shape[0])
    if(data.shape[0]<300): print("Continue")
    else:
        print("Nice try !!!!")
        return;                 
    #############      CLUSTERING       #################        
    lm= MyClust.Get_Clusters(data,num_clusters)                 #Data of all points will be clustered into some points
    lm2=  np.array(Euclid.fun1(lm,num_clusters))                #Distance array of all clusters
    #print(lm2)   
    lm2= Ham.Shortest_path_way(lm2,num_clusters)                #Order of the path it needed to travel
    #print(lm2)   
    lm2= np.array(lm2[0][:-1],dtype= np.int64)
    #print(lm2)
    mm= Ham.path_order(lm2,lm,num_clusters)                     #After sorting of the landmarks,path has been defined
    #print(mm)
    return(mm)                                                  #Returning path to comp2

def comp2(i):
    lbl= []
    mm= mm1= []    
    lbl.append(i)
    #print(i)
    for j in range(0,len(lbl)):
        xnum= 13
        try:
            mm1= newimg(i)                                      #Getting sorted path from the image
            #print(mm1)
        except:
            print("Error in comp2")                             #If any error occurs
            #print(lbl[i])
            #print(test_labels[lbl[i]])
        if(xnum < mm1[0,0]):                                    #Path will get reversed.Basically we need to take the number or Alphabet from top
            mm1= mm1[: :-1]       
        mm.append(mm1.reshape(num_clusters*2,).T)               #Transpose the obtained matrix
    #print(mm)
    return(mm)                                                  #Send this matrix to cr_small2

def cr_small2(cr_range,l1,select,Alphabet_Mapping_List,dict_num,dict_num1):
    img= l1[0]      
    listed= comp2(img)                                          #Getting from comp2
    dlist= dlist2 =[]                                           #Distance empty lists declarations
    if(select == 1):                                            #Alphabets will be selected
        for k in Alphabet_Mapping_List:                         #Alphabet_Mapping_List consists of all alphabets
            for l in range(dict_range):                         #Compares with all the optimized training test which is in dict_range
                dlist.append(distance.euclidean(listed[0], dict_num[k][l]))     #Obtaining 
    elif(select == 2):
        for i in range (10):
                for j in range(num_range):
                    dlist.append(distance.euclidean(listed[0], dict_num1[i][j]))
        #dlist.sort()
    dmin= int(dlist.index(min(dlist))/cr_range)                 #Getting the Number or Alphabets according to the cr_range
    #print(dmin)
    dlist2= copy.deepcopy(dlist)
    dlist2.sort()
    #print(dlist2[1])
    dmin2= int(dlist.index(dlist2[1])/cr_range)
    dmin3= int(dlist.index(dlist2[2])/cr_range)               
    sum=np.sum(dlist)                         #For getting average among the best three
    #print(np.float32(1/sum))
    #print(np.float32(sun1))
    if(select == 1):                                            #Prints in the terminal
        """ print("\nAlphabet Image: "+str(Alphabet_Mapping_List[dmin])+"\tConfidence: "+str(np.float32(100*(1-(dlist2[0]/sum))))+"%\n")
        print("Recognition  2: "+str(Alphabet_Mapping_List[dmin2])+"\tConfidence: "+str(np.float32(100*(1-(dlist2[1]/sum))))+"%")
        print("Recognition  3: "+str(Alphabet_Mapping_List[dmin3])+"\tConfidence: "+str(np.float32(100*(1-(dlist2[2]/sum))))+"%") """
        return(Alphabet_Mapping_List[dmin],Alphabet_Mapping_List[dmin2],Alphabet_Mapping_List[dmin3],str(np.float32(100*(1-(dlist2[0]/sum)))),str(np.float32(100*(1-(dlist2[1]/sum)))),str(np.float32(100*(1-(dlist2[2]/sum)))))

    if(select == 2):
        """ print("\nImage Number  : "+str(dmin)+"\tConfidence: "+str(np.float32(100*(1-(dlist2[1]/sum))))+"%\n")
        print("Recognition  2: "+str(dmin2)+"\tConfidence: "+str(np.float32(100*(1-(dlist2[1]/sum))))+"%")
        print("Recognition  3: "+str(dmin3)+"\tConfidence: "+str(np.float32(100*(1-(dlist2[1]/sum))))+"%") """
        return(dmin,dmin2,dmin3,str(np.float32(100*(1-(dlist2[0]/sum)))),str(np.float32(100*(1-(dlist2[1]/sum)))),str(np.float32(100*(1-(dlist2[2]/sum)))))

def func1(select):
    crrange=0
    dict_range= 700
    num_range= 600
    print("\nSairam")
    Alphabet_Mapping_List = list(string.ascii_uppercase)            #List of alphabets

    #path1 = "/FOLDERCR1/"                                 
    #print(os.getcwd())
    path1= os.getcwd()+"/FOLDERCR1/"                                #Path of the folder where images will be stored
    #print(path1)
    if not os.path.exists(path1):
        folder1= path1+ '/' + "Letter"                              #Path of the folder where Alphabet image will be stored
        folder2= path1+'/' + "Number"                               #Path of the folder where Number image will be stored
        os.makedirs(folder1)                                        #Directories will be created
        os.makedirs(folder2)
        print("Folders Created")
  
    #select= int(input("\n1.Alphabet\n2.Number\n\nChoose: "))       #Choice can be made
    print("\n--------------------------------------------\n\n")

    if(select ==  1):   
        crrange= dict_range                                        #Dictionary will be set to the Alphabet range(700)
        folder= path1+"Letter"                                     #Alphabet path will be selected
    elif(select ==  2):
        crrange= num_range                                          #Dictionary will be set to the Number range(600)
        folder= path1+"Number"                                     #Number path will be selected
    l1 = []
    #print(folder)
    for filename in os.listdir(folder):                             #Checks whether the folder exists or not
        try:
            img = mpimg.imread(os.path.join(folder, filename))      #Takes images from the mentioned folder
            if img is not None:                                     #If image is not none then it is appended to l1[]
                l1.append(img)
            #images = np.asarray(images)
        except:
            print("type of image is: ",type(img))                   #Prints the type of image
            print('Cant import ' + filename)                        #Filename that is not able to import
        l1 = np.asarray(l1)*255                                     #Changing the format to float which is in another format
        l1= l1.astype(int)                                          #After multiplying converting to int
        #print(type(img))      
    #print(l1)
    print("Testing with dict range: ",crrange)

    with open('n15d700file1000.p','rb') as handle:                  #700 different alphabets each from 1000 by clustering
        dict_num= p.load(handle)                                    #Storing in dictionary
    with open('n15d600.p','rb') as handle:                          #600 diffenrent numbers each from the testing set
        dict_num1= p.load(handle)                                   #Storing in dictionary1

    print("\n\n-----Input Dict_num(clusters is loaded-----\n")
    #print(len(dict_num['F']))
    """ graph.subplot(1, 2, 2)
    graph.imshow(255-l1[0], cmap = 'gray')        
    graph.show() """
    print("-----------Character recognition------------\n")
    v1,v2,v3,p1,p2,p3= cr_small2(crrange,l1,select,Alphabet_Mapping_List,dict_num,dict_num1)
    print("\n\n\n\n____________ENJOY SUCCESSFUL RECOGNISATION  TRY____________\n\n\n\n")
    return(v1,v2,v3,p1,p2,p3)

""" try:    
    select= int(input("\n1.Alphabet\n2.Number\n\nChoose: "))            #Choice can be made   
    v1,v2,v3,p1,p2,p3=func1(select)
except:
    print("Exception Occured") """

