import os, platform, socket
import subprocess as sb
import time

def configuration(ip_address, port_used):
    try:
        IP = ip_address
        PORT = port_used
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
    except ConnectionRefusedError:
        configuration()
    except ConnectionAbortedError:
        configuration()

def shell():
    os.system("cls")
    os_name = s.recv(5000)
    os_name = os_name.decode()
    os_version = s.recv(5000)
    os_version = os_version.decode()
    current_dir = s.recv(5000)
    current_dir = current_dir.decode()
    current_dir = current_dir + str(">")
    print(f"""Microsoft {os_name} [Version {os_version}]
Copyright(c) 2009 Microsoft Corporation. All right reserved.
            """)
    while True:
        try:
            command = str(input(f"{current_dir}" ))
            if command == ("clear") or command == ("cls"):
                os.system("cls")
                continue
            elif len(command) == 0:
                continue
            elif command == ("exit"):
                s.send(command.encode())
                s.close()
                break
            else:   
                s.send(command.encode())
            recv_command = s.recv(4000)
            recv_command = recv_command.decode()
            if recv_command == "not available":
                continue
            if ("change to") in recv_command:
                new_dir = recv_command.split()[2]
                current_dir = new_dir + str(">")
            elif len(recv_command) == 0:
                print("success")
            elif "Exception:" in recv_command:
                print(recv_command)
            elif "OSError:" in recv_command:
                print(recv_command)
            else:
                print(recv_command, "\n")

        except KeyboardInterrupt:
            print("\n")
            pass
        except EOFError:
            pass
        except ConnectionResetError:
            print("ConnectionResetError")
            time.sleep(2)
            return False
        except ConnectionAbortedError:
            print("ConnectionAbortedError")
            time.sleep(2)
            return False
        except OSError as e:
            print(str(e))
            time.sleep(2)
        except BrokenPipeError as v:
            print(str(e))
            time.sleep(2)
        except Exception as e:
            print(str(e))
            time.sleep(2)

os_types = []
def set_os_type():
    os_types.clear()
    os_type = s.recv(7000)
    os_type = os_type.decode()
    os_types.append(os_type)

def clear_screen():
    os_type = os_types[0]
    if os_type == "possix":
        os.system("clear")
    else:
        os.system("cls")

def start(ip_address, port_used):
    configuration(ip_address, port_used)
    set_os_type()
    clear_screen()
    shell()