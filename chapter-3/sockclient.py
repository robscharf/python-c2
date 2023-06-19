import socket

def session_handler():
    print(f'[+] Connecting to {host_ip}.')

    sock.connect((host_ip, host_port))
    print(f'[+] Connected to {host_ip}.')

    # receive, decode, print message
    message = sock.recv(1024).decode()
    print(message)

    # send message
    response = input('Message to send#> ')
    sock.send(response.encode())

    sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_ip = '127.0.0.1'
host_port = 2222

session_handler()