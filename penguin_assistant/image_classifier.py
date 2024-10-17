import cv2
import os
import torch
from torchvision import models, transforms
from PIL import Image

model = models.resnet50(pretrained=True)
model.eval()

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def classify_image(image_path, labels):
    image = Image.open(image_path)
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(image)

    _, predicted_idx = torch.max(outputs, 1)
    predicted_label = labels[predicted_idx.item()]

    return predicted_label

def capture_and_classify_image(labels):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    try:
        ret, frame = cap.read()
        if ret:
            temp_image_path = "image.jpg"
            cv2.imwrite(temp_image_path, frame)
            predicted_label = classify_image(temp_image_path, labels)
            print("Predicted value:", predicted_label)

            # Optionally return the predicted label
            return predicted_label

            os.remove(temp_image_path)
        else:
            print("Error: Could not capture image")

    except Exception as e:
        print("Error:", e)
    finally:
        cap.release()
