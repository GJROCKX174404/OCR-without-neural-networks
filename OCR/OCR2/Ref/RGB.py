from PIL import Image
import numpy as np
import matplotlib.image as mpimg
import os
x=5
y=14
value= 0
im = Image.open('Alpha/alphabet/F/F-1.png') # Can be many different formats.
print(im.mode)
print(np.array(im))
images= []

folder = "/home/bca3/Desktop/CR1/CR_KID_VER/Alphabets/Alpha2/alphabet/A"
        #folder = './your/folder/'

for filename in os.listdir(folder):
    try:
        img = mpimg.imread(os.path.join(folder, filename))
        if img is not None:
                images.append(img)
    except:
        print('Cant import ' + filename)
images = np.asarray(images)
print(images[0])
images[0]= np.array((images[0]*255))
print(images[0].astype(int))
""" image_Path = image_Folder_Path + '/' + last_digit_Name + '/' + str(last_digit_Name) + '-' + str(count) + '.png'
        new_image.save(image_Path) """
#pix = np.array(im.load())
#print(im.size)  # Get the width and hight of the image for iterating over
#print(pix)  # Get the RGBA Value of the a pixel of an image
#pix[x,y] = value  # Set the RGBA Value of the image (tuple)

#im.save('alive_parrot.png')  # Save the modified pixels as .png