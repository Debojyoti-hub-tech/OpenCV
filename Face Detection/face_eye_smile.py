import cv2
face_cascade = cv2.CascadeClassifier("Face Detection\models\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("Face Detection\models\haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("Face Detection\models\haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 6)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2) 

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
    """(100,150,80,80)
    (100,150) --> face starts
    w = 80 --> 180
    h = 80 --> 230
    """
    eyes = eye_cascade.detectMultiScale(roi_gray ,1.2, 5)
    if len(eyes) >0:
        cv2.putText(frame,"Eye Detected", (x,y-30), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0, 255), 2)
    
    smiles = smile_cascade.detectMultiScale(roi_gray ,1.3,5)
    if len(smiles) >0:
        cv2.putText(frame, "Smile Detected", (x, y-10),
            cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), 2)

    
    cv2.imshow("Detection engine", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
