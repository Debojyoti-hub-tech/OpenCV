import cv2

image = cv2.imread('OIP.png')

h,w,c = image.shape
print("Height:", h, "Width:", w, "Channels:", c)

# output : Height: 210 Width: 389 Channels: 3
