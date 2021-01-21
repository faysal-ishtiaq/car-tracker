import getpass


def get_data_path(filename: str) -> str:
    return '/home/{}/car-tracker/data/{}'.format(getpass.getuser(), filename)


def get_yolo_path(filename: str) -> str:
    return '/home/{}/car-tracker/yolov4/{}'.format(getpass.getuser(), filename)

