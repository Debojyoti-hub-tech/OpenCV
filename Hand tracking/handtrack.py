import cv2
import mediapipe as mp

mpHands = mp.solutions.hands
Hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

while cap.isOpened() :
    ret, frame = cap.read()
    if ret is None:
        print("No frames found")
        break

    con_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = Hands.process(con_frame)    

    if results.multi_hand_landmarks:
        for _ in results.multi_hand_landmarks: #hand in frame => _
           mpDraw.draw_landmarks(frame, _, mpHands.HAND_CONNECTIONS)



    cv2.imshow("Hand tracking basics", frame)

    if cv2.waitKey(1) & 0xFF  == ord("q"):
        print("Program Exited succefully")
        break
cap.release()
cv2.destroyAllWindows