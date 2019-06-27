import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('C:/Users/Cezeri_NPC/Desktop/opencv/haarcascades/haarcascade_frontalface_default.xml')

userName = input("Kullanıcı adı giriniz: ")

flag = 0

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    flag =flag+1
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (69, 139, 116), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 'Face', (x + 5, y + h - 5), font, 1, (69, 139, 116), 2, cv2.LINE_AA)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = gray[y:y + h, x:x + w]
        cv2.imwrite("C:/Users/Cezeri_NPC/Desktop/opencv/users/"+str(userName)+str(flag)+".jpg", frame[y:y+h, x:x+w])
        time.sleep(0.2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()