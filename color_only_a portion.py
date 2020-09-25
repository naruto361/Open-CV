import cv2 as cv
import numpy as np

img=np.zeros((512,512,3),np.uint8)
img[:]=255,0,0
img1=np.zeros((512,512,3),np.uint8)
img1[100:200,100:400]=255,0,0
cv.line(img,(0,0),(512,512),(0,255,0),5)
cv.imshow('full blue',img)
cv.line(img1,(100,100),(400,200),(0,255,0),3)
cv.imshow('potion is blue',img1)
cv.waitKey(0)
cv.destroyAllWindows()
