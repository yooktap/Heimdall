from ultralytics import YOLO
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, 1)
model = YOLO('gundetect.pt')
results = model('tcp://127.0.0.1:8888', stream=True, show=True)

while True:
    for result in results:
        boxes = result.boxes
        confidences = result.boxes.conf.numpy().flat
        if (len(confidences)) and confidences[0] >= 0.6:
            print(f"boxes: {confidences[0]}")
            GPIO.output(18, 0)
