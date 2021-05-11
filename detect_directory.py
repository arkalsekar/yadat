import cv2
import argparse
import os
import sys


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--InputDirectory', required=True, help="Input Directory of the Images")
ap.add_argument('-o', '--OutputDirectory', required=True, help="Output Directory to store the Images")
ap.add_argument('-c', '--Confidence', required=False, help="Minimum Confidence to detect faces", default=1.1)
args = vars(ap.parse_args())


# Getting the Directory of Images
rootdir = args['InputDirectory']
print("INFO - Found the Input Directory at ", rootdir)

dir = os.listdir(args['InputDirectory'])
print("INFO - Getting the Images From ", rootdir)

# Import the model
print("INFO - Loading the Model")
faceCascade = cv2.CascadeClassifier("model/haarcascade_frontalface_default.xml")

# directory to save the results of the images
resulted_dir = os.mkdir(args["OutputDirectory"])
print("INFO - Created ", args['OutputDirectory'], "to save the Face Detected Images")

for i in dir:
    if i.endswith('jpg') or i.endswith('png') or i.endswith('jpeg'):
        img_dir = os.path.join(rootdir, i)
        img = cv2.imread(img_dir)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Find the faces in our image
        faces = faceCascade.detectMultiScale(imgGray, 1.1 ,4)
        # faces = faceCascade.detectMultiScale2()s
        # Create bounding box around the faces that we have detected. So we need to loop through all the faces that we have detected.
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,256,0), 2)


        # cv2.imshow("Result", img)   
        detected_image_dir = os.path.join(args['OutputDirectory'], i)

        print("INFO - Saving Detected Faces at", detected_image_dir)
        cv2.imwrite(detected_image_dir, img)

        # cv2.waitKey(0)