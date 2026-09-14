
import cv2 

cam = cv2.VideoCapture(0)

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'mp4v')
recorder = cv2.VideoWriter('output120.mp4', codec, 50.0, (frame_width, frame_height))

while True:
    success, image = cam.read()

    if not success:
        print("Failed to capture video frame.")
        break

    cv2.flip(image,1,image)
    cv2.putText(image, "Recording...", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    recorder.write(image)
    cv2.imshow("Recording live video", image) 
  
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Stopping the recording.")
        break

cam.release()
recorder.release()
cv2.destroyAllWindows()