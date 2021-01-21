import cv2
import argparse
import logging
from utils import classifier

from utils.helper_functions import *

logger = logging.getLogger("ModelClassifier")
logging.basicConfig(level=logging.INFO)


def main(arguments):
    objects = []

    yolo_config = get_yolo_path('yolov4.cfg')
    yolo_weight = get_yolo_path('yolov4.weights')
    make_model_classifier = get_data_path('model-weights-spectrico-car-brand-recognition-mobilenet_v3-224x224-170620.mnn')
    make_model_labels = get_data_path('labels-makes.txt')

    logger.info(f"YOLO config filepath: {yolo_config}")
    logger.info(f"YOLO weight filepath: {yolo_weight}")

    logger.info(f"YOLO color classifier filepath: {make_model_classifier}")
    logger.info(f"YOLO color labels filepath: {make_model_labels}")

    net = cv2.dnn_DetectionModel(get_yolo_path('yolov4.cfg'), get_yolo_path('yolov4.weights'))
    net.setInputSize(608)
    net.setInputScale(1.0 / 255)
    net.setInputSwapRB(True)
    car_make_classifier = classifier.Classifier(
        make_model_classifier,
        make_model_labels
    )

    img = cv2.imread(arguments.filename, cv2.IMREAD_COLOR)

    if img is None:
        return {
            "status": "error",
            "message": "Invalid image."
        }

    classes, confidences, boxes = net.detect(img, confThreshold=0.1, nmsThreshold=0.4)
    for classId, confidence, box in zip(classes.flatten(), confidences.flatten(), boxes):
        if classId in [2, 5, 7]:
            if confidence > 0.3:
                left, top, width, height = box
                x1 = left
                x2 = left + width
                y1 = top
                y2 = top + height
                car_img = img[y1:y2, x1:x2]
                (make, make_confidence) = car_make_classifier.predict(car_img)
                rect = {"left": str(x1), "top": str(y1), "width": str(x2 - x1), "height": str(y2 - y1)}
                objects.append(
                    {
                        "make": make,
                        "make_prob": str(make_confidence),
                        "obj_prob": str(confidence),
                        "rect": rect
                    }
                )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    args = parser.parse_args()

    main(args)
