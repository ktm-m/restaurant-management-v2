import os

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic.v1 import BaseSettings
from constant.environment import env_path


class App(BaseModel):
    env: str
    port: str
    version: str


class AWS(BaseModel):
    access_key_id: str
    secret_access_key: str
    region: str


class AppConfig(BaseSettings):
    app: App
    aws: AWS


class Config:
    def __init__(self):
        load_dotenv(dotenv_path=env_path)
        self.config = AppConfig(
            app=App(
                env=os.getenv("APP_ENV"),
                port=os.getenv("APP_PORT"),
                version=os.getenv("APP_VERSION"),
            ),
            aws=AWS(
                access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
                region=os.getenv("AWS_REGION"),
            ),
        )


def init_config():
    return Config().config
