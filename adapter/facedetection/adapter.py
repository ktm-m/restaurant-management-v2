from typing import Sequence

import cv2

from constant.model import scale_factor, min_neighbors, min_size
from internal.port.outbound.face_detection import FaceDetectionPort


class Adapter(FaceDetectionPort):
    def __init__(self):
        pass

    # __init__ is a constructor

    def detect_faces(self, face_cascade: cv2.CascadeClassifier, frame) -> Sequence[Sequence[int]]:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.cvtColor() is used to convert an image from one color space to another
        faces = face_cascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors=min_neighbors,
                                              minSize=min_size, flags=cv2.CASCADE_SCALE_IMAGE)
        # cv2.CascadeClassifier.detectMultiScale() is used to detect objects in an image
        # scaleFactor is used to compensate for the objects that appear smaller due to distance
        # minNeighbors is used to specify how many neighbors each candidate rectangle should have to retain it
        # maxSize is used to specify the maximum possible object size
        # minSize is used to specify the minimum possible object size
        # flags is used to specify how the model is used

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # cv2.rectangle() is used to draw a rectangle around the detected face
        return faces


def new_adapter() -> FaceDetectionPort:
    return Adapter()
