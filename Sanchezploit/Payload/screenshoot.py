import cv2
import numpy as np
from PIL import ImageGrab
import time
import os

def capture():
    img = ImageGrab.grab(bbox=(0, 0, 1366, 768)) # x=100, y=10, w=500, h=5000
    img_np = np.array((img))
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)
    cv2.waitKey(1)
    time.sleep(2)
    cv2.destroyAllWindows()
    os.system("@echo off")
    os.system("pause")
capture()