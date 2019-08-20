import numpy as np
import urllib.request
import cv2


def check(url):
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    res = urllib.request.urlopen(url)
    image = np.asarray(bytearray(res.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.6,
        minNeighbors=5,
        minSize=(30, 30),
    )

    return bool(len(faces))