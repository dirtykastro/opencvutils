from pathlib import Path
import sys, cv2 

if len(sys.argv) == 1 :
    print("invert colors of  and copies them to current folder")
    print("Usage: " + sys.argv[0] + " file_to_convert ")
    sys.exit(0)

file_path = sys.argv[1]

if Path(file_path).exists() and Path(file_path).is_dir() == False:

	face_cascade = cv2.CascadeClassifier(
	    #'./haarcascades/haarcascade_frontalface_default.xml')
	    #'./haarcascades/haarcascade_frontalface_alt.xml')
	    './haarcascades/haarcascade_frontalface_alt2.xml')
	    #'./haarcascades/haarcascade_frontalface_alt_tree.xml')
	img = cv2.imread(file_path)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 3, 3)
	for (x, y, w, h) in faces:
	    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)

	profileface_cascade = cv2.CascadeClassifier(
	    './haarcascades/haarcascade_profileface.xml')

	faces = profileface_cascade.detectMultiScale(gray, 1.5, 3)
	for (x, y, w, h) in faces:
	    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


	#cv2.imshow('Faces Detected!', img)
	#cv2.waitKey(0)
	cv2.imwrite("/home/kastro/HiddenDesktop/photosopencv/face.jpg", img)

else:
    print ("File %s doesn't exist" % file_path)

