
#*******************************************************************************************************************|
                                    #GUI INTERFACE FOR OPTICAL CHARACTER RECOGNITION                                |
#*******************************************************************************************************************|
'''Description: 
            The Gui INterface is created using Python Tkinter and  PIL.In the Main method the root is created,
            which acts as a Parent window for rest of the widgets.The  object of Class interface is invoked.
            The Following are the steps Executed by this GUI Interface Program:
                1)THe introduction animation is displayed and then the GUI is  created for Cahrqacter Recognition
                2)THe  are Two modes ,Based on which Predicton algoritm is performed.
                    (i)  Alphabet Mode (used for Prediction of UpperCase Alphabets(A-Z)).
                    (ii) Number Mode    (used for Prediction of  Number from dfigits (1-9)).
                  These modes has been implemented using RadioButton method
                  The user has to select any one of the mode.
                3)Then user can draw a his desired Character (Alphabet/Number) on the Drawing Canvas.
                    (i)The user then can press Predict button for Character Prediction
                    (ii)The Canvas saves a drawn Image in respective Folder based on the mode selected by the user.                  
                    (iii)The Prediction algortim  selects the image stored in the Folder and loads the image in the Optical Character reconition  pro 
                    (iv)The results of the prediction algoritm is returned to GUI program 
                4) the Character recognized  as by the Computer is Displayed in the Output box.
                    The Character is Recognized!!!.
                5)For reseting Canvas  CLear Button   is clicked

                The user can repeat the above steps for recognizing new Characters.'''






#********************************************************* PACKAGE INPORTS   ****************************************
''' Here the required   packages  are imported to  Avail the use of methods of DIffenrent LIbraries which include Tkinter,PIL.

Tkinter provides Python applications with an easy-to-program user interface.
It  is used for creating GUI WIdgets or Window objects like Window ,buttons ,Canvas .

Python Imaging Library (PIL) to used  create, display, and enhance images.
It includes loading  image objects from a variety of file formats (jpg,png,ppm etc)  and apply a rich set of image operations to them( such as resize,save,crop,etc).
'''
import tkinter as tk             #import tkinter Library
from tkinter import *            #import all methods avcailable in Tkinter Library
import PIL                       #Import PIL  
from PIL import ImageTk, Image, ImageDraw,ImageSequence   


#*****************************          IMPLEMENTATION OF Interface class  *************************************

'''    ***********************       INTRO       *********************************             
 The  class Interface  is invoked by the main method with root as parent window.

This means that all the widgets  created in this class will be displayed on the root(parent window) create in the Main Method.
'''

''' IN the Class Inerrface , a Master Canvas is created,on which other Widgets such as Button,Drawing Canvas.. wiill be placed.
    the Canvas is itself palced on the root window'''

''' The widgets to be displayed   are first  arranged and established  in their respective positions by using the Geomentry Manager Grid.
    The Grid manager arranges  the widgets in  specific postions defined by th row and column value.
    All these widgets are placed on the Master Canvas by specifying their (x,y) coordinates in the window '''
''' 
    the __init__ method of the class is used to initialize all the Properties of Object of class Interface such as color,IMage,Height ,Width.
    Also Master canvas is created on which Widgets can be Displayed.This itself in on the root(Parent Window).
    The default method  __init__ then  calls  "call()" functyion  to display a small LOading animation using Image and Gif.
    Then call1() is call to  execute Draw-Wigets method.THis methods controls all widets to be displaye don the canvas(buttons,Drawing canvas,RadiopButton) ''' 


class Interface(tk.Tk):                      ##AN Interface  class for Character Reconition for displaying widgets like Canvas,Button,Slider. 
    def __init__(self,master):
        self.master=master                   ##the orginal parent window master initialised to represent the master window contolling Interface Class
        
        self.color_fg = 'white'              ##forground  color is initalised to white.   This setting is used for the Drawing Marker color of canvas
        
        self.color_bg = 'black'              ##background  color is initalised to black.   This setting is used for the backround color of canvas
        
        self.Image="Images/bg521.jpg"              ##Background image of the application
        self.Predimg="Images/pred2.png"          ##IMage for Predict Icon
        self.CLRimg="Images/clr3.png"            ##IMage for CLear Icon
        self.Drwimg="Images/drwhere.png"         ##Additional  Image Draw Here
        self.opimg="Images/hh.png"               ##Additional Image for OUTPUT
        self.Alp="Images/Al.png"                 ##Image for Alphabet icon
        self.No="Images/no.png"                  ##Image for Number icon
        self.M_HEIGHT=700                        ##the height of Backround Image 
        self.M_WIDTH=1150                        ##THe Width of background Image
        
        #Creating a main background Canvas of respective Width and Height.
        ##The Sub widgets like Drawing Area,Prdict Button Output BOX etc is placed above the canvas. 
        self.master_canvas=Canvas(self.master,width=self.M_WIDTH,height=self.M_HEIGHT,bg="black")

        #master _csnvas Positoning 
        self.master_canvas.grid(row=0,column=0) 
        ###################################   SETTING BACKGROUND IMAGE OVER 'master_canvas' and configuring other images  #####################################            
        
        self.img=ImageTk.PhotoImage(Image.open(self.Image).resize((self.M_WIDTH, self.M_HEIGHT), Image.ANTIALIAS))
        self.Pred_img=ImageTk.PhotoImage(Image.open(self.Predimg).resize((120, 50), Image.ANTIALIAS))
        self.Clr_img=ImageTk.PhotoImage(Image.open(self.CLRimg).resize((120, 50), Image.ANTIALIAS))
        self.Drw_img=ImageTk.PhotoImage(Image.open(self.Drwimg).resize((200, 40), Image.ANTIALIAS))
        self.op_img=ImageTk.PhotoImage(Image.open(self.opimg).resize((482,50),Image.ANTIALIAS))
        self.Alp_img=ImageTk.PhotoImage(Image.open(self.Alp).resize((150,60),Image.ANTIALIAS))
        self.No_img=ImageTk.PhotoImage(Image.open(self.No).resize((150,60),Image.ANTIALIAS))

        
        ##########################################################################################################################
        
        self.old_x = None           #Previous  X Coordinate Initialised to None.
        self.old_y = None           #Previous  y Coordinate Initialised to None.
        self.black=(0)              #SET BLACK COLOR BY SPECIFYING VALUE 0
        self.white=(255)            #SET WHITE COLOR BY SPECIFYING VALUE 255
        self.Choice=None            #SET CHOICE TO NONE.USED for to make choice Between ALPHABET  AND NUMBER
        self.penwidth =24           #set PEnwidth of drawing canvas
        self.file=None              #varaible file is a path where saved casnvas image is located 


        #the Image sequence repeatedly displays the image , in a way to display animation gif.
        self.sequence = [ImageTk.PhotoImage(img.resize((280, 280))) 
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'Images/fff.gif'))]
        
        self.image = self.master_canvas.create_image(500,350, image=self.sequence[0])
        self.animate(1)
        self.master_canvas.after(1500,self.call1)
        self.master_canvas.after(4000,self.call)
        
    ########################################        HERE THE DRAWING CANVAS IS CREATED.          ######################################
    ######################################         Each time user Draws on this interface , line coordinates gets recorded
    ''' this function calls drawWidgets() to implement  GUI interface.'''  
    def call(self):
        self.bg = self.master_canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        self.drawWidgets()          #call method drawWidgets to create all Sub widgets
        #This method performs all neccessary operation of canvas ,when Image is drawn on it.
        self.Canvas_control()
    ########################################        HERE THE DRAWING CANVAS IS CREATED.          ######################################    
    def Canvas_control(self):
            
        self.bg = self.master_canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        self.drawWidgets()          #call method drawWidgets to create al Sub widgets
        self.c.bind('<B1-Motion>',self.paint)              
        self.c.bind('<ButtonRelease-1>',self.reset)
        self.image1 = PIL.Image.new("RGB", (300, 300), self.black)   #setting the Drawing Canvas
        self.draw = ImageDraw.Draw(self.image1)                      #Enable Drawing on canvas 
    def call1(self):
        self.Image3="Images/py2.png"
        self.imgitr=ImageTk.PhotoImage(Image.open(self.Image3).resize((1000,750), Image.ANTIALIAS))
        self.master_canvas.create_image(500,350,image=self.imgitr)
     
    ###################################### IN paint method, each time user Draws on this interface , line coordinates gets recorded and displayed on the canvas   ##########
    def paint(self,e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x,self.old_y,e.x,e.y,width=self.penwidth,fill=self.color_fg,capstyle=ROUND,smooth=True)
            self.draw.line([self.old_x, self.old_y, e.x,e.y],fill="white",width=40)
        self.old_x = e.x
        self.old_y = e.y
    
    ####################################This methos is responsibl efor  Small Introductary Loading Animation ######################################################################################
    def animate(self, counter):
        self.master_canvas.itemconfig(self.image, image=self.sequence[counter])
        self.master.after(20, lambda: self.animate((counter+1) % len(self.sequence)))


    def reset(self,e):
        self.old_x = None
        self.old_y = None      

    def changeW(self,e):
        self.penwidth = e


##################################      IN The save Method , the drawn Image is saved in specific folder.            ##########################
##################################      If the Choice is ALphabet --->Letter FOlder                              ##########################
##################################      If the Choice is number --->Number FOlder                               ##########################
    def save(self):
        self.output.delete('1.0',END)
        print(self.Choice)
        if(self.Choice==1):
            self.file = "FOLDERCR1/Letter/image1.png"
        elif(self.Choice==2):
            self.file= "FOLDERCR1/Number/image1.png"
        if self.file:
            x = self.master.winfo_rootx() + self.c.winfo_x()
            y = self.master.winfo_rooty() + self.c.winfo_y()
            x1 = x + self.c.winfo_width()
            y1 = y + self.c.winfo_height()

            self.image1.save(self.file )                                    ##Image is saved in Specific Folder
            self.load_img=Image.open(self.file)                             ## Saved IMage is reopened from the  folder
            self.load_img=self.load_img.resize((28,28), Image.ANTIALIAS)    ##RE-Size Image
            self.load_img = self.load_img.convert('L')                      ## Image is coverted to Greyscale
            self.load_img.save(self.file)                                   ##Image is saved in same folder
            
        import main1 as cr                                             ##import main1 program containing the Predicting Algoritm
        
        try:
            v1,v2,v3,p1,p2,p3=cr.func1(self.Choice)			   ##Executing Prdicting Algoritm (BACKEND)
            #print(v1,v2,v3,p1,p2,p3)
	    ######The Prediction results obtained from the Prediction algoritm is displayed in  the Output Box      ########
            self.output.insert(tk.INSERT,"\n   -----------CHARACTER RECOGNITION-----------\n\nFIRST GUESS     : {}      Confidence: {}%\n\nSECOND GUESS : {}     Confidence: {}%\n\nThird GUESS      : {}      Confidence:{}%\n\n".format(v1,p1,v2,p2,v3,p3))
        except:
            self.output.insert(tk.INSERT," \n\nUnrecognisable Character\n\nSorry ...!  Good try !!!!\n\nPlease Try Again")

#################################################################################################################

    
    ##A method to select choice between Alphabet And Number
    def sel(self):                      
        
        self.Choice=self.s.get()        ##this records the Choice selected By user 

    
    ##A method used to Clear  the Drawing Canvas ###############
    def clear(self):                                
        
        self.c.delete(ALL)                          #Delete all Drawings on the Drawing Canvas
        self.draw.rectangle((0,0,300,300),fill=(0)) #Repaints the Drawing Canvas with Black color
        self.output.delete('1.0',END)               #Delete Previous output textbox.


 ###################      This Method is used to create RadioButtons ,Buttons SLider  the Drawing Canvas and the Output Box.
 ####################      All the Widgets are placed on the main Background Canvas.        
    def drawWidgets(self):
        
        self.DrawHere=Label(image=self.Drw_img)
        self.wind_drw=self.master_canvas.create_window(100,20,anchor=tk.NW, window=self.DrawHere)
        
        #THe Radio Buttons which selects mode(ALphabet/Number) are created and configured and placed on Master canvas
        self.s=IntVar()
        self.r1=Radiobutton(self.master,indicator =0,image=self.Alp_img,variable=self.s,value=1,activebackground="light goldenrod",foreground="black",font=('Noto Sans CJK JP Bold',14),selectcolor="blue",command=self.sel,bd=3,cursor='hand1')
        self.r2=Radiobutton(self.master,indicator = 0,image=self.No_img,variable=self.s,value=2,activebackground="light goldenrod",foreground="black",font=('Noto Sans CJK JP Bold',14),selectcolor="red",bd=3,command=self.sel,cursor='hand1')
        self.wind2=self.master_canvas.create_window(420, 100, anchor=tk.NW, window=self.r1)
        self.r1.config(padx=15,pady=10)
        self.wind3=self.master_canvas.create_window(420, 200, anchor=tk.NW, window=self.r2)
        self.r2.config(padx=15,pady=10)

        # Drawing Canvas is created and updated ,placed on Master Canvas .
        self.c = Canvas(self.master,width=380,height=300,bg=self.color_bg)
        self.wind4=self.master_canvas.create_window(20, 60, anchor=tk.NW, window=self.c)

        #Predict Button is created ,positioned on the Master Canvas and then Configured
        self.Predict=Button(image=self.Pred_img,command=self.save,font=('',12),bd=1)
        self.wind5=self.master_canvas.create_window(90, 380, anchor=tk.NW, window=self.Predict)

        #Clear Button is created ,positioned on the Master Canvas and then Configured
        self.Clear=Button(image=self.Clr_img,bd=-1,command=self.clear)
        self.wind6=self.master_canvas.create_window(230, 380, anchor=tk.NW, window=self.Clear)

        #Output Textbox is created ,positioned on the Master Canvas and then Configured
        self.output_label=Label(self.master,image=self.op_img)
        self.winop=self.master_canvas.create_window(30,450,anchor=tk.NW,window=self.output_label)
        self.output=tk.Text(self.master,bg='White',foreground='Black',height=9,width=48,font=('',12))
        self.output.grid(row=6,column=0)
        self.win7=self.master_canvas.create_window(30,500,anchor=tk.NW,window=self.output)
       
        
################################           MAIN METHOD             ####################################

''' Here the parent window root is created .Also an object of "INterface"  class is created where the Grapical Wingets are  configured.
     Also the properties of the root  are Configured such as Size ,Title ,Background Image And Iconphoto.
     The root.mainloop keeps executing program ,until user Explicitly terminates the program'''      

        
if __name__ == '__main__':
    root = Tk()             #THe parent "root" Window is created
    root.geometry("1000x700")     #The size of root is given by its Geomentric Dimensions (Width,Height)        
    GUI=Interface(root)           #AN Obejct of class Interface is created .This class is responsible to Create Subwidgets such as Button,Label,Drawing Canvas.   
    root.title('DrawingApp')      #The Title of  GUI APPLICATION 
    root.configure(background='grey17')     #Background color of root window 
    root.iconphoto(root,PhotoImage(file="Images/tk.png"))     #THe Icon Photo  of the Application  

    root.mainloop()              #THe mainloop executes program  until user exits the Application









