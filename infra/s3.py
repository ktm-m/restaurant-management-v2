import boto3
from infra.config import AWS


class S3:
    def __init__(self, aws_config: AWS):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_config.access_key_id,
            aws_secret_access_key=aws_config.secret_access_key,
            region_name=aws_config.region,
        )


def new_s3(aws_config: AWS) -> S3:
    return S3(aws_config=aws_config).s3_client
