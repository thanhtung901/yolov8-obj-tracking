import torch

model = torch.hub.load('best.pt')
img = 'img.png'
res = model(img)
print(res)