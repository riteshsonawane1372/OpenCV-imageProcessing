# we are going to create multiple window 

from tkinter import Frame
from turtle import width
import cv2
from cv2 import COLOR_BAYER_BG2BGR_VNG

# we are going to solve this by using matrix so by using rows and columns and taking input from the user 

rows = int(input("how much rows do you want ?"))
columns = int(input("how many columns do you want ?")) # taking the input from user for no. of rows and columns 


width =450    
height =500               
om = cv2.VideoCapture(0,cv2.CAP_DSHOW) 
om.set(cv2.CAP_PROP_FRAME_WIDTH,width)   
om.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
om.set(cv2.CAP_PROP_XI_FRAMERATE,30)
om.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore,rrs = om.read()
    rrs = cv2.resize(rrs,(int(width/columns),int(height/rows))) # resize the window acc to the i/p of rows and columns dont forget to use int bcoz it dont take str...

    # and if any error in above code which is line no. 24 then see the bracket does the value of x and y are in paranthesis 

    for i in range (0,rows):  # using nested for loop starting from 0 to rows
        for j in range (0,columns): 
            windownName ='window'+str(i)+'x'+str(j) # to show window we should have differnet name so here we are creating a variable and 
            # adding str value of i and j so it gets all unique values
            cv2.imshow(windownName,rrs) #showing thoses windows and the frame 
            # now the main thing is arrangements so for that we will use the below 
            # so this will move the columns and rows * and j and i respectly a
            # sometimes the content gets hidden so we are adding 30px more to the rows 

            cv2.moveWindow(windownName,int(width/columns)*j,int(height/rows+30)*i)   
            
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

om.release()   
