import cv2
import numpy as np

x = input("Hangi video ?")
cap = cv2.VideoCapture('car'+ x +'.mp4')

y = input("Hangi tür ?")
y=1

if(y==1):
    car_cascade = cv2.CascadeClassifier('C:/Users/Cezeri_NPC/Desktop/opencv/haarcascades/cars.xml')
else:
    car_cascade = cv2.CascadeClassifier('C:/Users/Cezeri_NPC/Desktop/opencv/haarcascades/haarcascade_frontalface_default.xml')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in cars:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 'Car', (x + 5, y + h - 5), font, 1, (255, 0, 0), 1, cv2.LINE_AA)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = gray[y:y + h, x:x + w]

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()


