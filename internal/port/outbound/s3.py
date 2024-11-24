from abc import ABC, abstractmethod

import cv2


class S3Port(ABC):
    @abstractmethod
    def load_model(self, bucket_name: str, key: str) -> cv2.CascadeClassifier:
        pass
