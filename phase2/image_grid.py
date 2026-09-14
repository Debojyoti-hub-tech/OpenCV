import cv2

# Load image
img = cv2.imread("OIP.png")

# Grid size (pixels)
grid_size = 50

height, width = img.shape[:2]

# Draw vertical lines
for x in range(0, width, grid_size):
    cv2.line(img, (x, 0), (x, height), (0, 255, 0), 1)

# Draw horizontal lines
for y in range(0, height, grid_size):
    cv2.line(img, (0, y), (width, y), (0, 255, 0), 1)

# Show image
cv2.imshow("Grid Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()