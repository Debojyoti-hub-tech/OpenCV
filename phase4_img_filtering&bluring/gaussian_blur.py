import cv2

image =  cv2.imread("env.jpg")
rimage = cv2.resize(image, (500, 500))

blurred = cv2.GaussianBlur(rimage, (9, 9), 3)

print("Image shapes", rimage.shape)

cv2.imshow('Original Image', rimage)
cv2.imshow('Blurred Image', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()