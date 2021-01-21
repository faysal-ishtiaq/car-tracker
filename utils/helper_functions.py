import os


def get_data_path(filename: str) -> str:
    return '/home/%s/car-tracker/data/%s'.format(os.getlogin(), filename)


def get_yolo_path(filename: str) -> str:
    return '/home/%s/car-tracker/yolov4/%s'.format(os.getlogin(), filename)

