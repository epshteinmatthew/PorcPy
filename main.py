from audioop import avg
from traceback import print_tb
from types import NoneType
import cv2 as cv
import sys

import numpy as np

#TODO-ACCURATE COLOR RANGES

def turnAmount(totaldeg, width, centerx):
    return (totaldeg*(centerx/width))-totaldeg/2



img = cv.imread("circles.jpg")
if img is None:
    sys.exit("Could not read the image.")
image = cv.cvtColor(img, cv.COLOR_BGR2HSV )

dest = cv.inRange(image, np.array([160,100,100]), np.array([179,255,255]))
dest = cv.GaussianBlur(dest, (3,3),cv.BORDER_DEFAULT)
cv.imshow("Display window", dest)
k = cv.waitKey(0)
circles = cv.HoughCircles(dest,cv.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)
if type(circles) == NoneType:
    print("Whouopsy daisy")
    quit()                           
circles = np.uint16(np.around(circles))
avgx = np.uint16(0)
avgy = np.uint16(0)
lenny = 0
if len(circles) == 1:
    print("found some cirlces")
for i in circles[0,:]:
    # draw the outer circle
    cv.circle(dest,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(dest,(i[0],i[1]),2,(0,0,255),3)
    avgx += i[0]
    avgy += i[1]
    lenny += 1
avgx //= lenny
avgy //= lenny

cv.circle(dest, (avgx, avgy),4, (0,0,255), 5)
print(turnAmount(35, dest.shape, avgx)[0])

cv.imshow("Display window", dest)
k = cv.waitKey(0)
quit()