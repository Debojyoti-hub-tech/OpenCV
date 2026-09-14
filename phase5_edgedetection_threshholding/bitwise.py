import cv2
import numpy as np

# IMAGE1 and 2 height and weight be same
# use only grayscale color
# 
img1 = np.zeros((300,300, 1), dtype=np.uint8)
img2 = np.zeros((300,300, 1), dtype=np.uint8)

cv2.circle(img1, (150,150), 100, 255, -1)
cv2.rectangle(img2, (100,100), (250,250), 255, -1)

bitand= cv2.bitwise_and(img1, img2)
bitor= cv2.bitwise_or(img1, img2)
bitnot= cv2.bitwise_not(img2)

cv2.imshow("AND", bitand)
cv2.imshow("OR", bitor)
cv2.imshow("NOT", bitnot)
cv2.waitKey()
cv2.destroyAllWindows()