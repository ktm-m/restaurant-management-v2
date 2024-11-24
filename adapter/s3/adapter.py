import os.path

import boto3
import cv2

from constant.model import face_cascade_model
from internal.port.outbound.s3 import S3Port


class Adapter(S3Port):
    def __init__(self, s3_client: boto3.client):
        self.s3_client = s3_client

    def load_model(self, bucket_name: str, key: str) -> cv2.CascadeClassifier:
        if not os.path.exists(face_cascade_model):
            obj = self.s3_client.get_object(Bucket=bucket_name, Key=key)

            model_data = obj['Body'].read()
            # obj['Body'].read() is used to read the content of the object

            with open(face_cascade_model, 'wb') as model_file:
                model_file.write(model_data)
                # open() is used to open a file in binary write mode
                # model_file.write() is used to write the content of the model_data to the file

        return cv2.CascadeClassifier(face_cascade_model)
        # cv2.CascadeClassifier() is used to load the cascade classifier model


def new_adapter(s3_client: boto3.client) -> S3Port:
    return Adapter(s3_client=s3_client)
