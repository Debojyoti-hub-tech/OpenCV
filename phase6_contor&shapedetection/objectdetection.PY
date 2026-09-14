import cv2

# Read and resize image
img = cv2.imread("hexagon.jpg")
rimg = cv2.resize(img, (500, 500))

# Convert to grayscale
gray = cv2.cvtColor(rimg, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

# Find contours (OpenCV 4.x style)
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    print(0.01 * cv2.arcLength(contour, True))
    corners = len(approx)
    
    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        shape_name = "Quadrilateral"
    elif corners == 5:
        shape_name = "Pentagon"
    elif corners == 6:
        shape_name = "Hexagon"
    elif corners == 7:
        shape_name = "Heptagon"
    elif corners == 8:
        shape_name = "Octagon"
    elif corners == 9:
        shape_name = "Nonagon"
    elif corners == 10:
        shape_name = "Decagon"
    else:
        shape_name = "Circle"
    
    cv2.drawContours(rimg, [approx], 0, (0, 0, 255), 2)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    cv2.putText(rimg, shape_name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
# Show result
cv2.imshow("Detected Contours", rimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
