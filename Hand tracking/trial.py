import cv2
import mediapipe as mp

# Initialize Holistic model
mpHolistic = mp.solutions.holistic
holistic = mpHolistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Drawing utilities
mpDraw = mp.solutions.drawing_utils

# Drawing styles for clarity
draw_spec_landmarks = mpDraw.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=2)
draw_spec_connections = mpDraw.DrawingSpec(color=(0,0,255), thickness=1, circle_radius=2)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("No frames found")
        break

    # Convert BGR to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = holistic.process(rgb_frame)

    # Draw face landmarks (468 points)
    if results.face_landmarks:
        mpDraw.draw_landmarks(
            frame,
            results.face_landmarks,
            mpHolistic.FACEMESH_TESSELATION,
            draw_spec_landmarks,
            draw_spec_connections
        )
        mpDraw.draw_landmarks(
            frame,
            results.face_landmarks,
            mpHolistic.FACEMESH_CONTOURS,
            draw_spec_landmarks,
            draw_spec_connections
        )

    # Draw hand landmarks (21 points each hand)
    if results.left_hand_landmarks:
        mpDraw.draw_landmarks(
            frame,
            results.left_hand_landmarks,
            mpHolistic.HAND_CONNECTIONS,
            draw_spec_landmarks,
            draw_spec_connections
        )
    if results.right_hand_landmarks:
        mpDraw.draw_landmarks(
            frame,
            results.right_hand_landmarks,
            mpHolistic.HAND_CONNECTIONS,
            draw_spec_landmarks,
            draw_spec_connections
        )

    # Draw pose landmarks (33 points)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(
            frame,
            results.pose_landmarks,
            mpHolistic.POSE_CONNECTIONS,
            draw_spec_landmarks,
            draw_spec_connections
        )

    cv2.imshow("Holistic Tracking (Face + Hands + Pose)", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Program exited successfully")
        break

cap.release()
cv2.destroyAllWindows()
