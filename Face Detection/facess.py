import cv2
import time
import os

# ==========================
# Load Haar Cascades
# ==========================
FACE_MODEL = "Face Detection/models/haarcascade_frontalface_default.xml"
EYE_MODEL = "Face Detection/models/haarcascade_eye.xml"
SMILE_MODEL = "Face Detection/models/haarcascade_smile.xml"

face_cascade = cv2.CascadeClassifier(FACE_MODEL)
eye_cascade = cv2.CascadeClassifier(EYE_MODEL)
smile_cascade = cv2.CascadeClassifier(SMILE_MODEL)

if face_cascade.empty():
    raise FileNotFoundError("Face cascade not found!")

if eye_cascade.empty():
    raise FileNotFoundError("Eye cascade not found!")

if smile_cascade.empty():
    raise FileNotFoundError("Smile cascade not found!")

# ==========================
# Webcam
# ==========================
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

prev_time = 0
frame_count = 0

print("Press Q to Quit")
print("Press S to Save Screenshot")

# ==========================
# Main Loop
# ==========================
while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Mirror view
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=6,
        minSize=(80, 80)
    )

    face_count = len(faces)

    # --------------------------
    # Face Loop
    # --------------------------
    for (x, y, w, h) in faces:

        # Face Rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

        cv2.putText(
            frame,
            "Face",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # --------------------
        # Eyes
        # --------------------
        eyes = eye_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.15,
            minNeighbors=8,
            minSize=(25,25)
        )

        if len(eyes) > 0:

            cv2.putText(
                frame,
                "Eyes Detected",
                (x, y+h+25),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255,0,0),
                2
            )

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(
                roi_color,
                (ex, ey),
                (ex+ew, ey+eh),
                (255,0,0),
                2
            )

        # --------------------
        # Smile
        # --------------------
        smiles = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.7,
            minNeighbors=20,
            minSize=(40,40)
        )

        if len(smiles) > 0:

            cv2.putText(
                frame,
                "Smile Detected",
                (x, y+h+50),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0,255,255),
                2
            )

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(
                roi_color,
                (sx, sy),
                (sx+sw, sy+sh),
                (0,255,255),
                2
            )

    # ==========================
    # FPS Calculation
    # ==========================
    current_time = time.time()
    fps = 1 / (current_time - prev_time) if current_time != prev_time else 0
    prev_time = current_time

    # ==========================
    # HUD
    # ==========================
    cv2.rectangle(frame, (0,0), (340,110), (40,40,40), -1)

    cv2.putText(
        frame,
        f"FPS : {int(fps)}",
        (10,30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,0),
        2
    )

    cv2.putText(
        frame,
        f"Faces : {face_count}",
        (10,60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,255,255),
        2
    )

    cv2.putText(
        frame,
        "Press Q = Quit",
        (10,90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0,200,255),
        2
    )

    cv2.imshow("Face Detection Engine", frame)

    key = cv2.waitKey(1) & 0xFF

    # Save Screenshot
    if key == ord('s'):
        filename = f"screenshot_{int(time.time())}.png"
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")

    # Quit
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()