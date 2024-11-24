from abc import ABC, abstractmethod
from typing import Sequence


class FaceDetectionPort(ABC):
    @abstractmethod
    def init_camera(self):
        pass

    @abstractmethod
    def release_camera(self):
        pass

    @abstractmethod
    def detect_faces(self, frame) -> Sequence[Sequence[int]]:
        pass
