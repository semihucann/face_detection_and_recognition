import cv2, os
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("C:/Users/Cezeri_NPC/Desktop/opencv/haarcascades/haarcascade_frontalface_default.xml")

myPath = ("C:/Users/Cezeri_NPC/Desktop/opencv/users/")
usernames =["1","2","3","4","5"]


def getImagesAndLabels():
    # get the path of all the files in the folder
    imagePaths=[]
    # create empth face list
    faceSamples = []
    # create empty ID list
    Ids = []
    for i in usernames:
        tmp = myPath
        tmp += i

        for f in os.listdir(tmp):
            imagePaths.append(tmp + "/" + f)
            # loading the image and converting it to gray scale
            pilImage = Image.open(tmp + "/" + f).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(i)
            # extract the face from the training image sample
            faces = detector.detectMultiScale(imageNp)
            # If a face is there then append that in the list as well as Id of it
            for (x, y, w, h) in faces:
                faceSamples.append(imageNp[y:y + h, x:x + w])
                Ids.append(Id)

    return faceSamples, Ids

faces,Ids = getImagesAndLabels()
recognizer.train(faces, np.array(Ids))
recognizer.save('C:/Users/Cezeri_NPC/Desktop/opencv/arda.yml')
