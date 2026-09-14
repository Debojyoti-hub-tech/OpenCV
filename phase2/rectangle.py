import cv2

image = cv2.imread("OIP.png")

if image is not None:
    p1 = (50,50)
    pt2 = (250,200)
    color = (120, 25, 210)  # Green color in BGR
    thickness = 4
    cv2.rectangle(image, p1, pt2, color, thickness) 
    cv2.imshow("Image with Rectangle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not read the image.")




