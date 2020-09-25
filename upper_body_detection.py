import cv2 as cv
import numpy as np

upper_cascade=cv.CascadeClassifier('haarcascade_upperbody.xml')
#lower_cascade=cv.CascadeClassifier('haarcascade_lowerbody.xml')
cap=cv.VideoCapture('vtest.avi')

while 1:
    _,frame=cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces=upper_cascade.detectMultiScale(gray,1.2,4)
    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
    
    cv.imshow('frame',frame)
    k=cv.waitKey(1)
    if k==27:
        break
cap.release()
cv.destroyAllWindows()
        
    