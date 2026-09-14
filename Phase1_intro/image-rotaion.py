import cv2
image = cv2.imread("OIP.png")

# # Rotate the image by 90 degrees
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE) # type: ignore


if image is None:
    print("Error: Could not read the image.")

else:
    h, w = image.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center,45, 1.0)

    rotated = cv2.warpAffine(image, M, (w,h))
    cv2.imshow("Original", image)
    cv2.imshow("R1", rotated_image)
    cv2.imshow("R2", rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()