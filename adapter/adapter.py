import boto3

from adapter.s3.adapter import new_adapter as new_s3_adapter
from adapter.facedetection.adapter import new_adapter as new_face_detection_adapter


class Adapters:
    def __init__(self, s3_client: boto3.client):
        self.s3_adapter = new_s3_adapter(s3_client=s3_client)
        self.face_detection_adapter = new_face_detection_adapter()


def new_adapters(s3_client: boto3.client) -> Adapters:
    return Adapters(s3_client=s3_client)
