from ultralytics import YOLO

model = YOLO('best.pt')

model.fuse()
# model.init(verbose=False)
model.export(format = 'onnx')


