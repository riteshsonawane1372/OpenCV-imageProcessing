

# IN this homework we need to display the frame rate on the left side 



# This program is incomplete kindly see Lesson 8




















from re import T
from tkinter import W
import time # imporint the time liabr
import cv2
print(cv2.__version__)

text =" hi how are u "




camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH,640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
camera.set(cv2.CAP_PROP_FPS,30)
camera.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

tlast =time.time()  # knowing what timw it was exceuted

# sso the kick here is that the frame fps is same has the while true means the hole 1 true loop is one fps 


while True:
    dt= time.time()-tlast # dt i sthe time it takes to go through the loop 
    showtimw = str(dt*100.010010010)
    tlast =time.time()
    ignore,frame = camera.read()
    
    frame_rate =str(cv2.CAP_PROP_FRAME_COUNT)

    cv2.rectangle(frame,(250,140),(390,220),(0,255,0),2)
    cv2.circle(frame,(250,140),25,(255,255,255)) 
    cv2.putText(frame,showtimw,(20,60),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    cv2.imshow('My window',frame)
    if cv2.waitKey(1)==ord('r'):
        break

camera.release()