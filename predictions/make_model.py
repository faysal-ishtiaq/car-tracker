import cv2
import argparse

from utils import classifier


def main(arguments):
    objects = []

    net = cv2.dnn_DetectionModel('../yolov4/yolov4.cfg', '../yolov4/yolov4.weights')
    net.setInputSize(608)
    net.setInputScale(1.0 / 255)
    net.setInputSwapRB(True)
    car_make_classifier = classifier.Classifier(
        '../data/model-weights-spectrico-car-brand-recognition-mobilenet_v3-224x224-170620.mnn',
        '../data/labels-makes.txt'
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
