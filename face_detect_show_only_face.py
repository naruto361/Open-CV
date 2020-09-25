import cv2 as cv
face_cascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv.VideoCapture(0);
while cap.isOpened():
    ret,frame=cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    frame2=frame[y:y+h,x:x+w]
    cv.imshow('frame',frame)
    cv.imshow('frame2',frame2)
    k=cv.waitKey(1)
    if k==27:
        break
cap.release()
cv.destroyAllWindows()