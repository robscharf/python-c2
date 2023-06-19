import socket

host_ip = 'localhost'
host_port = 2222

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

print(f'[+] Connecting to {host_ip}.')

sock.connect((host_ip, host_port))
print(f'[+] Connected to {host_ip}.')

sock.close()