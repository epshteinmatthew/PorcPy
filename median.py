# put image to multidimensional array
# go thru each pixel(for loop), keep row and col number
# if row or col is 0 or array length, continue
# otherwise make an array of values surrounding the selected value
# sort the array
# take the median(array[len/2])
# put median for the pixel
# do this with list comprehension?(cant bcuz numpy)

# Import the necessary libraries
from email.mime import image
from PIL import Image
import cv2 as cv
import sys
import numpy

#define vars, turn to grayscale
window_rad = 2
count = 0
imeg = cv.imread("thing.jpeg")
if imeg is None:
    sys.exit("Could not read the image.")
image = cv.cvtColor(imeg, cv.COLOR_BGR2GRAY)
cv.imwrite("thig.jpeg", image)
img = Image.open("thig.jpeg")
np_img = numpy.array(img)

#mainloop(fix speed issue, nditer)
for i in range(len(np_img)):
    # edit this for variable input
    if i <= window_rad or i >= len(np_img) - (window_rad+1):
        count += 1
        continue
    for x in range(len(np_img[i])):
        if x <= window_rad or x >= len(np_img[i]) - (window_rad+1):
            count += 1
            continue
        neighs = np_img[i-window_rad:i+(window_rad+1), x-window_rad:x+(window_rad+1)]
        result = neighs.flatten()
        result.sort()
        np_img[i, x] = result[len(result)//2]


data = Image.fromarray(np_img)
      
    # saving the final output 
    # as a PNG file
data.save('gfg_dummy_pic.jpeg')
