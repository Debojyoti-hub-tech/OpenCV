import cv2
import numpy as np

image =  cv2.imread("env.jpg")
rimage = cv2.resize(image, (500, 500))

# Define a simple sharpening kernel
kernel = np.array([[0, -1, 0],
                   [-1,  5, -1],
                   [0, -1, 0]])

sharpened = cv2.filter2D(rimage, -1, kernel)

print("Image shapes", rimage.shape)

cv2.imshow('Original Image', rimage)
cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()