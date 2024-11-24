import logging

import cv2

from adapter.adapter import new_adapters
from infra.config import init_config
from internal.service.service import new_services, Services
from infra.s3 import new_s3


def process_frame(services: Services, frame):
    faces = services.face_detection_service.detect_faces(frame)
    print(faces)
    cv2.imshow('face detection', frame)
    # cv2.imshow() is used to display an image in a window


def main():
    app_config = init_config()
    s3_client = new_s3(app_config.aws)
    adapters = new_adapters(s3_client=s3_client)
    services = new_services(s3_adapter=adapters.s3_adapter, face_detection_adapter=adapters.face_detection_adapter)

    cap = services.face_detection_service.init_camera()
    if cap is None:
        logging.warning('cannot open a camera')
        return

    try:
        while True:
            ret, frame = cap.read()
            # cap.read() is used to read the video frame
            if not ret:
                break

            process_frame(services=services, frame=frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        services.face_detection_service.release_camera()


if __name__ == '__main__':
    main()
