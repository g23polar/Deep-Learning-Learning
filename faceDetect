import cv2
from glob import glob

shop_images = glob('/Users/gaut/Desktop/General/CS/py/py/DeepLearning/face_images/*.jpg')
"""
Detects faces using OpenCV
"""
def detectFaces(pics):
    cnt = 0
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    for picture in shop_images:
        cnt += 1
        print(cnt)
        img = cv2.imread(picture)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(image=gray, minNeighbors=4, minSize=(40,40), scaleFactor=1.5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

        cv2.imshow('img', img)
        cv2.waitKey(delay=25)

detectFaces(shop_images)
