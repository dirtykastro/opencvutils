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

    while(cap.isOpened()):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',gray)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

else:
    print ("File %s doesn't exist" % file_path)

