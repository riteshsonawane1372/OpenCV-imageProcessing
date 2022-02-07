# creating an checkbox using openCV and numpy 
from re import T
from tkinter import Frame
from turtle import color
import cv2
import numpy as np

Size_of_board = int(input(" PLS enter the size of board you want"))+50 # taking the size of board from user 

numsquare = int(input(" How many the square")) # taking the no. square fromuser

square_board_size = int(Size_of_board/numsquare) # defining the board size  and coverting it to an integer to avoid error 

#setting the color 

darkcolor = (0,0,0)
lightcolor =(255,255,255)
nowcolor =darkcolor

while True:
    
    x=np.zeros([Size_of_board,Size_of_board,3],dtype=np.uint8)
    #going through the rows and cloumns and checking the color starting with row 

    for row in range(0,numsquare):
        for column in range(0,numsquare):
            x[square_board_size*row:square_board_size*(row+1),square_board_size*column:square_board_size*(column+1)] = nowcolor
            if nowcolor==darkcolor:  # checking the color to make it alternative
                nowcolor=lightcolor
            else:
                nowcolor=darkcolor
        if nowcolor ==darkcolor: # reflip the color for next row 
            nowcolor=lightcolor 
        else:
            nowcolor=darkcolor

    cv2.imshow("board" ,x)
    if cv2.waitKey(1) ==ord('r'):
        break



    