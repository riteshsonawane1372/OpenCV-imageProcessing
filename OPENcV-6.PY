from re import T
from tkinter import W
import cv2
print(cv2.__version__)

text =" hi how are u "

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH,640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
camera.set(cv2.CAP_PROP_FPS,30)
camera.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:

    ignore,frame = camera.read()
    # frame[140:220,250:390] =(255,255,255)
    # adding rectangle to farme 
    cv2.rectangle(frame,(250,140),(390,220),(0,255,0),2) # play around this para
    cv2.circle(frame,(250,140),25,(255,255,255)) # adding circle around ur frame 
    cv2.putText(frame,text,(120,60),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),2) # putting text on ur window 
    cv2.imshow('My window',frame)
    if cv2.waitKey(1)==ord('r'):
        break

camera.release()