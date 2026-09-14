import cv2

image = cv2.imread("OIP.png")

if image is not None:
    cv2.putText(image, "Hello, OpenCV!", (140, 190),
                 cv2.FONT_HERSHEY_SIMPLEX, 1, (180, 45, 120), 2, cv2.LINE_AA)
    cv2.imshow("Image with Text", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()