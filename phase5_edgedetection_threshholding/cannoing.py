import cv2

rimage =  cv2.imread("OBJ.webp")


edge = cv2.Canny(rimage, 100, 150)

print("Image shapes", rimage.shape)
print("Edge shapes", edge.shape)

cv2.imshow('Original Image', rimage)
cv2.imshow('Edge Image', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()