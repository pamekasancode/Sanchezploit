import socket
import os, sys
import time

def config(ip_address, port_used):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, port_used))

def send_messege(messege):
    sending_messge = s.send(messege.encode())
    if not send_messege:
        return False
    else:
        return True

def chating():
    name = str(input("your name here> "))
    s.send(name.encode())
    while True:
        try:
            msg = str(input(f"{name}>"))
            s.send(msg.encode())
        except ConnectionAbortedError:
            return False
        except ConnectionResetError:
            return False
        except ConnectionError:
            return False
        except BrokenPipeError:
            return False
        except KeyboardInterrupt:
            pass
        except EOFError:
            confirm = str(input("disconnect the network? "))
            if "y" in confirm:
                print("disconnecting the network...")
                time.sleep(0.5)
                send_halt = s.send(str("halt0x332").encode())
                if not send_halt:
                    print("failed to request shutdown!")
                    time.sleep(0.5)
                    print("exiting the script")
                else:
                    print("success to disconnect the network!")
                return
            else:
                pass

def start(ip_address, port_used):
    config(ip_address, port_used)
    chating()
    s.close()
