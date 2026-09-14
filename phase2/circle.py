import cv2

image = cv2.imread("OIP.png")

if image is not None:
    h,w,c = image.shape
    cv2.circle(image, (w//2,h//2), w//4, (0, 255, 0), 2)  # Draw a circle with center (200,200) and radius 100
    cv2.imshow("Image with Circle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()