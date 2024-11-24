from abc import ABC, abstractmethod
from typing import Sequence

import cv2


class FaceDetectionPort(ABC):
    # Abstract Base Class (ABC)
    @abstractmethod
    def detect_faces(self, face_cascade: cv2.CascadeClassifier, frame) -> Sequence[Sequence[int]]:
        pass
