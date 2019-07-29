# Face Authentication with LBPH Algorithm

## Introduction

> Local Binary Pattern (LBP) is a simple yet very efficient texture operator which labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number.

![](https://github.com/semihucann/face_Authentication_with_LBPH/blob/master/algo.jpg)

##### More information about the alorithm
[Face Recognition: Understanding LBPH Algorithm](https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b)

## Usage

### personDetect.py
People's faces and eyes are detected by haarcascade. 

### faceRecognation.py
The code creates datasets to train from people faces.

### faceTrainer.py
The code creates trained data (.yml) from datasets.

### faceAuthantication.py
The code provides to authentication.

