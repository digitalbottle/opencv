import numpy as np
import cv2
from imutils import perspective
# for four_point_transform 

image=cv2.imread('1.jpg',1)
print(image.shape)
# check the size and format for original image, which can help with parameter adjustment
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# read the image and turn it from rgb 2 gray
gradX=cv2.Sobel(gray,ddepth=cv2.cv.CV_32F,dx=1,dy=0,ksize=-1)
gradY=cv2.Sobel(gray,ddepth=cv2.cv.CV_32F,dx=0,dy=1,ksize=-1)
# set ksize=-1 to use Schar, which turns out to have best performance among different kinds of kernel
# gradient=cv2.subtract(gradX,gradY) was taken into consideration but
# turned out to be not satisfying, especially for rotation case, so we abandon it
gradient=cv2.add(gradX,gradY)
cv2.imshow('Gradient',gradient)
cv2.waitKey(0)
blurred=cv2.blur(gradient,(6,6))
# Image Smoothing: blur the image before binary with thresh to avoid disturbance of QR code
# Since a QR code contains more holes
# Kernel size should be adjusted many times
cv2.imshow('Blur',blurred)
cv2.waitKey(0)
(_,thresh)=cv2.threshold(blurred,200,255,cv2.THRESH_BINARY)
# thresh_binary the image
cv2.imshow('Binary',thresh)
cv2.waitKey(0)
kernel=cv2.getStructuringElement(cv2.MORPH_RECT, (21,7))
close=cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
# close once
cv2.imshow('Close', close)
cv2.waitKey(0)
# kernel size adjusted several times to fit 3 images 
erose=cv2.erode(close,None,iterations=7)
# erose
cv2.imshow('Erose',erose)
cv2.waitKey(0)
dilat=cv2.dilate(erose,None,iterations=7)
# dilation for seven times
cv2.imshow('Dilate',dilat)
cv2.waitKey(0)
# print(dilat.dtype)
dilat = cv2.convertScaleAbs(dilat)
# print(dilat.dtype)
# convert scale before paint contour
(cnts,_)=cv2.findContours(dilat.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# cv2.CHAIN_APPROX_SIMPLE aims at a rectangular contour 
c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
rect = cv2.minAreaRect(c)
box = np.int0(cv2.cv.BoxPoints(rect))
# obtain 4 points
cv2.drawContours(image, [box], -1, (255, 0, 0), 3)
# paint the box with blue lines
cv2.imshow('Result',image)
cv2.waitKey(0)
cv2.imwrite("./Result.jpg", image)
# write the result into a new file
new = perspective.four_point_transform(image,box.reshape(4, 2))
cv2.imshow('Barcode',new)
cv2.waitKey(0)
cv2.imwrite("./Barcode.jpg", image)
cv2.imwrite("./Final.jpg", new)
