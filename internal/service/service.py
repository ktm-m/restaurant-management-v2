from internal.port.outbound.face_detection import FaceDetectionPort
from internal.port.outbound.s3 import S3Port
from internal.service.facedetection.service import new_service


class Services:
    def __init__(self, s3_adapter: S3Port, face_detection_adapter: FaceDetectionPort):
        self.face_detection_service = new_service(s3_adapter=s3_adapter, face_detection_adapter=face_detection_adapter)


def new_services(s3_adapter: S3Port, face_detection_adapter: FaceDetectionPort) -> Services:
    return Services(s3_adapter=s3_adapter, face_detection_adapter=face_detection_adapter)
