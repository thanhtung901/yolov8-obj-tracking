from ultralytics import YOLO
import numpy as np

from PIL import Image

model = YOLO("best.pt")


results = model.predict(source='./video1.mp4', show = True, save = True, classes = 2)
