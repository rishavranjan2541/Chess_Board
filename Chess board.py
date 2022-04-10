# CHESS BOARD 8X8

from cv2 import COLOR_BGR2HLS
import numpy as np
import cv2

# making the background black
img = np.zeros((800,800,3))
for i in range(4):
    row = 200*i # odd rows
    row2 = row +100 # even rows
    for j in range(4):
        col = 200*j  # odd columns
        col2 = col + 100 # even columns
        img[row:(row+100), col:(col+100)]= 255,255,255
        img[row2:(row2+100), col2:(col2+100)]= 255,255,255
        
cv2.imshow('CHESS BOARD',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
