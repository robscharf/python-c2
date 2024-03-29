import socket

def session_handler():
    print(f'[+] Connecting to {host_ip}.')
    sock.connect((host_ip, host_port))
    print(f'[+] Connected to {host_ip}.')

    while True:
        try:
            print('[+] Listening for response...')
            # receive, decode, print message
            message = sock.recv(1024).decode()

            if message == 'exit':
                print ('[-] Server terminated session.')
                sock.close()
                break

            print(message)

            # send message
            response = input('Message to send#> ')
            if response == 'exit':
                sock.send(response.encode())
                sock.close()
                break

            sock.send(response.encode())
        
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

host_ip = '127.0.0.1'
host_port = 2229

session_handler()