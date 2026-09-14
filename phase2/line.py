import cv2

image = cv2.imread("OIP.png")

if image is not None:
    p1 = (50,100)
    pt2 = (300, 100)
    color = (0, 255, 0)  # Green color in BGR
    thickness = 4
    # cv2.line(image, p1, pt2, color, thickness)
    cv2.rectangle(image, p1, pt2, color, thickness) 
    cv2.imshow("Image with Line", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not read the image.")










# class reverse:
#     def __init__(self, arr):
#         self.arr = arr

#     def reverse(self):
#         f, l = 0, len(self.arr) - 1
#         while f < l:
#             self.arr[f], self.arr[l] = self.arr[l], self.arr[f]
#             f += 1
#             l -= 1

# x = [10,20,30,40,50]
# r = reverse(x) #class object created
# r.reverse()
# print(x)


# import keyboard
# import pyautogui
# import time

# def automate_keys_and_clicks():
#     last_mouse_click = time.time()
    
#     while True:
#         # Press E every 5 seconds
#         keyboard.press_and_release('e')
#         print("Pressed E")
#         time.sleep(3*60)

#         # Check if 7 minutes have passed since last mouse click
#         if time.time() - last_mouse_click >= 6*60 :
#             pyautogui.click()  # Left mouse click
#             print("Clicked left mouse button")
#             last_mouse_click = time.time()

# if __name__ == "__main__":
#     automate_keys_and_clicks()
