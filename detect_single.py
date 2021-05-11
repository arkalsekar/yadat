import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input', required=True, help="Path of the Input Image")
ap.add_argument('-o', '--output', required=True, help="Path of the Output Image")
args = vars(ap.parse_args())

# Import the model
faceCascade = cv2.CascadeClassifier("model/haarcascade_frontalface_default.xml")
img = cv2.imread(args['input'])
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Find the faces in our image
faces = faceCascade.detectMultiScale(imgGray,1.1,4)
# faces = faceCascade.detectMultiScale2()
# Create bounding box around the faces that we have detected. So we need to loop through all the faces that we have detected.
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,256,0), 2)

cv2.imwrite(args['output'], img)
cv2.imshow("Result", img)
cv2.waitKey(0)
