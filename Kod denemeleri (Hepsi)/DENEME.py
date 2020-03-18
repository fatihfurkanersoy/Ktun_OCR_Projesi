import tesseract
import cv2
import cv2 as cv
import numpy as np

image0=cv2.imread("1.png")

offset=20
height,width,channel = image0.shape
image1=cv2.copyMakeBorder(image0,offset,offset,offset,offset,cv2.BORDER_CONSTANT,value=(255,255,255))

cv2.namedWindow("Test")
cv2.imshow("Test", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()