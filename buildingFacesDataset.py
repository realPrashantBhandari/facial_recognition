import cv2
import dlib
import os

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
ids = input("Enter New User ID(random 6 digit number): ")
total = 1
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
        ## create a folder called datset in your working directory
        cv2.imwrite("dataset/"+str(ids)+".jpg",frame[y1-20:y2+30,x1-20:x2+30])
        break
      

cv2.destroyAllWindows()
cap.release()
