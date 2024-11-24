from typing import Sequence

import cv2

from internal.port.outbound.face_detection import FaceDetectionPort as OutboundFaceDetectionPort
from internal.port.inbound.face_detection import FaceDetectionPort as InboundFaceDetectionPort
from internal.port.outbound.s3 import S3Port
from constant.s3 import model_bucket_name, face_cascade_key


class Service(InboundFaceDetectionPort):
    def __init__(self, s3_adapter: S3Port, face_detection_adapter: OutboundFaceDetectionPort):
        self.cap = None
        self.s3_adapter = s3_adapter
        self.face_detection_adapter = face_detection_adapter

    def init_camera(self):
        for i in range(10):
            self.cap = cv2.VideoCapture(i)
            # cv2.VideoCapture() is used to capture video from the camera
            if self.cap.isOpened():
                return self.cap

        return None

    def release_camera(self):
        if self.cap is not None:
            self.cap.release()
            cv2.destroyAllWindows()
            # cv2.destroyAllWindows() is used to close all windows

    def detect_faces(self, frame) -> Sequence[Sequence[int]]:
        face_cascade = self.s3_adapter.load_model(bucket_name=model_bucket_name, key=face_cascade_key)
        return self.face_detection_adapter.detect_faces(face_cascade=face_cascade, frame=frame)


def new_service(s3_adapter: S3Port, face_detection_adapter: OutboundFaceDetectionPort) -> InboundFaceDetectionPort:
    return Service(s3_adapter=s3_adapter, face_detection_adapter=face_detection_adapter)
