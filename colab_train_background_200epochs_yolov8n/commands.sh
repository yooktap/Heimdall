libcamera-vid -n -t 0 --framerate 1 --inline --listen -o tcp://127.0.0.1:8888
yolo detect predict model=gundetect.pt source=tcp://127.0.0.1:8888 show=True
