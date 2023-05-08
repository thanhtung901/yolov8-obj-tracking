from ultralytics import YOLO
def train():
# Load the model.
    model = YOLO('/home/linhnt/Desktop/yolov8s/KHDL/yolov8s.pt')

    # Training.
    results = model.train(
        data='/home/linhnt/Desktop/yolov8s/KHDL/utd2-5/data.yaml',
        imgsz=640,
        epochs=50,
        batch=16,
        name='/home/linhnt/Desktop/yolov8s/KHDL/kq')
if __name__ == '__main__':
    train()
