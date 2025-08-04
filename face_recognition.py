import numpy as np 
import cv2 as cv
import os

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# features = np.load('features.npy',allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread('C:\\Users\\piule\\OneDrive\\Desktop\\Projects\\opencv\\img\\dipika\\download (2).jpg')

#mapping the labels to names
people = []
for i in os.listdir('C:\\Users\\piule\\OneDrive\\Desktop\\Projects\\opencv\\img'):
    people.append(i)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('person', gray)

#detect faces in the image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]


    label, confidence = face_recognizer.predict(faces_roi)

    print(f'Label: {people[label]} with a confidence of {confidence}')


    
    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)



cv.imshow('detected Face', img)

cv.waitKey(0)