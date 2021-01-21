import os


def get_data_path(filename: str) -> str:
    return '/home/{}/car-tracker/data/{}'.format(os.getlogin(), filename)


def get_yolo_path(filename: str) -> str:
    return '/home/{}/car-tracker/yolov4/{}'.format(os.getlogin(), filename)

