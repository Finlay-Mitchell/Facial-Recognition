# I'm not exactly experienced in Python and this probably isn't neat code, but it was a fun project to work on.

import cv2

faceCascade = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")  # Loads up file for face detection.
location = ""  # Gets the video stream.
cv2.namedWindow("IPWebcam")  # Create a window.
vc = cv2.VideoCapture(location)  # Get the video capture from the URL.

if not vc.isOpened():
    print("Can't open this video stream location")
    exit()

while True:
    ret, frame = vc.read()  # Read the data.
    fps = vc.get(cv2.CAP_PROP_FPS)  # This gets the framerate of the video stream.

    faces = faceCascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB), scaleFactor=1.1, minNeighbors=5,
                                         minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)  # Detects the faces.

    # Draws the rectanges around the detected faces.
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Face detected', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)  # Labels face

    cv2.putText(frame, str(fps), (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255, 255), 2)  # Shows the FPS count.
    cv2.imshow("IPWebcam", frame)  # Displays the image.

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Waits for the user to press 'q' before exiting the program.
        break

# Release the capture.
vc.release()
cv2.destroyAllWindows()  # Exit the window.
