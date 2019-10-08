import dlib
import cv2
import numpy as np
import os
import face_recognition

cap = cv2.VideoCapture(0)

total = 1
dataset_img = os.listdir('dataset')
detector = dlib.get_frontal_face_detector()

while True:
    _,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:

        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        cv2.rectangle(frame, (x1-20,y1-20),(x2+30,y2+30), (0,255,255), 3)
        
        total += 1

    cv2.imshow("Frame",frame)

    cv2.waitKey(1)
    if total == 10:
        cv2.imwrite("test.jpg",frame)
        break


new_image = face_recognition.load_image_file('test.jpg')
new_image_encoded = face_recognition.face_encodings(new_image)[0]

for image in dataset_img:
    current_img = face_recognition.load_image_file("dataset/" + image)
    current_img_encoded = face_recognition.face_encodings(current_img)[0]
    result = face_recognition.compare_faces([new_image_encoded],current_img_encoded)

    
    if result[0] == True:
        base = os.path.basename('dataset/'+image)
        person_id = os.path.splitext(base)[0]
        print ("matched: " + person_id)
    else:
        base = os.path.basename('dataset/'+image)
        person_id = os.path.splitext(base)[0]
        print ("Not Matched: " + person_id)
        

cap.release()
cv2.destroyAllWindows()
