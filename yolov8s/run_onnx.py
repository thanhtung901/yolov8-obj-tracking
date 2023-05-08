# !pip install onnx onnxruntime-gpu
import onnx, onnxruntime
from PIL import Image
from torchvision import transforms
import torch

import numpy as np
img_path = 'img.png'
model_name = 'best.onnx'
onnx_model = onnx.load(model_name)
onnx.checker.check_model(onnx_model)

image = Image.open(img_path)
resize = transforms.Compose(
                [ transforms.Resize((640,640)), transforms.ToTensor()])
image = resize(image)
image = image.unsqueeze(0) # add fake batch dimension
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print("device", device)
image = image.to(device)

EP_list = ['CUDAExecutionProvider', 'CPUExecutionProvider']

ort_session = onnxruntime.InferenceSession(model_name, providers=EP_list)

def to_numpy(tensor):
      return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()

# compute ONNX Runtime output prediction
ort_inputs = {ort_session.get_inputs()[0].name: to_numpy(image)}
ort_outs = ort_session.run(None, ort_inputs)

arr = np.array(ort_outs)
print(arr[0][0].shape)
from matplotlib import pyplot as plt
plt.imshow(arr[0][0], interpolation='nearest')
plt.show()

