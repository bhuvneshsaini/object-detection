import torch


# Load YOLOv5 model and replace the yolov5s.pt weights path with your weights location path
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/bhuvn/Downloads/yolov5s.pt', source='local')
