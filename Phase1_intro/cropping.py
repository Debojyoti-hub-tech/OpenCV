import cv2
import numpy as np

image = cv2.imread("OIP.png")
 
cropped = image[50:200, 100:300] # pyright: ignore[reportOptionalSubscript, reportArgumentType, reportCallIssue]

cv2.imshow('Original Image', image) # pyright: ignore[reportArgumentType, reportCallIssue]
cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()