import socket

host_ip = 'localhost'
host_port = 2222

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

sock.bind((host_ip, host_port))
print('[+] Awaiting connection...')

sock.listen()

remote_target, remote_ip = sock.accept()

print(f'[+] Connection recieved from {remote_ip}')

remote_target.close()
