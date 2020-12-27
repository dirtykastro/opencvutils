#!python

from pathlib import Path
import sys, cv2 

if len(sys.argv) == 1 :
    print("transform images to jpg and copies them to current folder")
    print("Usage: " + sys.argv[0] + " file_to_convert ")
    sys.exit(0)

file_path = sys.argv[1]

if Path(file_path).exists() and Path(file_path).is_dir() == False:
    file_name = Path(file_path).stem
    file_extension = Path(file_path).suffix.lower()

    jpg_extensions = [".jpg", ".jpeg"]

    if file_extension in jpg_extensions : 
        print ("File %s is already jpg" % (Path(file_path).name))
    else:
        image = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
        cv2.imwrite(file_name + ".jpg", image)
        

else:
    print ("File %s doesn't exist" % file_path)
