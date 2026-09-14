import cv2

image = cv2.imread('OIP.png') 

if image is not None:
    cv2.imshow('Image', image) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # cv2.imwrite('output_image.png', image) #to save image 
else:
    print("Error: Image not found or unable to load.") 