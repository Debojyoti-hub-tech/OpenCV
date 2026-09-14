import cv2

img = cv2.imread("hexagon.jpg")
rimg = cv2.resize(img, (500, 500))
gray = cv2.cvtColor(rimg, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray,200,255, cv2.THRESH_BINARY)

# Find contors(Tells python the borders of the image)
contors, hierchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

# cv2.drawContours(image, contours, countourIdx, color, thickness) # Draw the contors on the image
cv2.drawContours(rimg, contors, -1, (0, 255, 0), 3) # Draw the contors on the image
cv2.imshow("Original Image", rimg)
cv2.waitKey(0)
cv2.destroyAllWindows()









# import sqlite3

# with sqlite3.connect("book.sql") as connection:
#     cursor = connection.cursor()
#     query = """ CREATE TABLE BOOKS(
#              id INTEGER,
#              title TEXT)"""
#     query1 = """INSERT INTO BOOKS(id, title) VALUES(102, 'Python Programming')"""
#     cursor.execute(query1)
#     connection.commit()

#     cursor.execute("SELECT * FROM BOOKS")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)