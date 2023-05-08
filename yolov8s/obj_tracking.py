import cv2
import argparse

from ultralytics import YOLO
import supervision as sv
import numpy as np
from supervision.tools.line_counter import LineCounter
from supervision.geometry.dataclasses import Point


LINE_START = Point(50, 1500)
LINE_END = Point(3790, 1500)

line_counter = LineCounter(start=LINE_START, end=LINE_END)
def main():
    frame_width, frame_height = [1280, 720]
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    model = YOLO("best.pt")

    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=2,
        text_scale=1
    )
    while True:
        ret, frame = cap.read()

        result = model(frame, agnostic_nms=True, classes = 2)[0]
        detections = sv.Detections.from_yolov8(result)
        line_counter.update(detections=detections)
        labels = [
            f"{model.model.names[class_id]} {confidence:0.2f}"
            for _, confidence, class_id, _
            in detections
        ]
        frame = box_annotator.annotate(
            scene=frame,
            detections=detections,
            labels=labels
        )
        frame = box_annotator.annotate(scene=frame, detections=detections, labels=labels)
        cv2.imshow("yolov8", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()