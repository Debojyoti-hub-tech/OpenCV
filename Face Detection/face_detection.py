import cv2
import time
face_cascade = cv2.CascadeClassifier("Face Detection\models\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 6)
    """
    detectMultisacle() --> scan and detect faces
    1.1 = scale factor --> balanced, not too slow
    5 = min Neighbours --> Test if that's a face
    3 __> loose checking
    5__> safe checking
    6__> strict checking 
    """

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2) 
        """
        x,y - top-left corner
        (x+w, y+h) - bottom-right corner
        eg - face1 = (100,150,80,80)
        top left - (100,150)
        x - how far from left, y - top , w - width, h - height"""
  
    cv2.imshow("Webcam Face Detected", frame)
         
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting the video stream.")
        break

cap.release()
cv2.destroyAllWindows()


