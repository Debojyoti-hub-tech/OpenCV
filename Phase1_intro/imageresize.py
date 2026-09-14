import cv2

image = cv2.imread("OIP.png")


resized =  cv2.resize(image,(200,300)) # pyright: ignore[reportArgumentType, reportCallIssue]

cv2.imwrite('resized_image.png', resized)
cv2.imshow('Original Image', image) # pyright: ignore[reportArgumentType, reportCallIssue]
cv2.imshow('Resized Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()