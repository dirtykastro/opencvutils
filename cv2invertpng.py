#!python

from pathlib import Path
import sys, cv2 

if len(sys.argv) == 1 :
    print("invert colors of  and copies them to current folder")
    print("Usage: " + sys.argv[0] + " file_to_convert ")
    sys.exit(0)

file_path = sys.argv[1]

if Path(file_path).exists() and Path(file_path).is_dir() == False:
    file_name = Path(file_path).stem
    file_extension = Path(file_path).suffix.lower()

    if file_extension == ".png" : 
        image = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)

        width = image.shape[0]
        height = image.shape[1]

        for column_index in range(0, width):
            for row_index in range(0, height):
                pixel = image[column_index, row_index]

                image[column_index, row_index] = [255 - pixel[0], 255 - pixel[1], 255 - pixel[2], pixel[3]]

        cv2.imwrite(file_name + "_inverted.png", image)
    else:
        print ("File %s is not a png" % (Path(file_path).name)) 

else:
    print ("File %s doesn't exist" % file_path)

