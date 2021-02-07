from pathlib import Path
import sys
import numpy as np
import cv2

if len(sys.argv) == 1 :
    print("play video")
    print("Usage: " + sys.argv[0] + " file_to_play ")
    sys.exit(0)

file_path = sys.argv[1]

if Path(file_path).exists() and Path(file_path).is_dir() == False:

    cap = cv2.VideoCapture(file_path)

    face_cascade = cv2.CascadeClassifier(
        #'./haarcascades/haarcascade_frontalface_default.xml')
        #'./haarcascades/haarcascade_frontalface_alt.xml')
        #'./haarcascades/haarcascade_frontalface_alt2.xml')
        './haarcascades/haarcascade_frontalface_alt_tree.xml')
    profileface_cascade = cv2.CascadeClassifier(
        './haarcascades/haarcascade_profileface.xml')


    while(cap.isOpened()):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, w, h) in faces:
            frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

        faces = profileface_cascade.detectMultiScale(gray, scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, w, h) in faces:
            frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)


        cv2.imshow('frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

else:
    print ("File %s doesn't exist" % file_path)

