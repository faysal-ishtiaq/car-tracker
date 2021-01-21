import os


def get_data_path(filename: str) -> str:
    return f"/home/{os.getlogin()}/car-tracker/data/{filename}"


def get_yolo_path(filename: str) -> str:
    return f"/home/{os.getlogin()}/car-tracker/yolov4/{filename}"

