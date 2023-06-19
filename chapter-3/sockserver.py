import socket

def listener_handler():

	# instantiate websocket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# bind websocket to host ip/port
	sock.bind((host_ip, host_port))
	print('[+] Awaiting connection from client...')
	
	# set socket to listen and accept connections from the address declared in app variables
	sock.listen()
	
	remote_target, remote_ip = sock.accept()
	# use {remote_ip[0]} to omit port from print statement
	print(f'[+] Connection received from {remote_ip}')

	while True:
		try:
			# capture and send message
			message = input('Message to send#> ')
			remote_target.send(message.encode())

			# receive and print message
			response = remote_target.recv(1024).decode()
			print(response)

		except Exception:
			remote_target.close()
			break


	# capture and send message
	message = input('Message to send#> ')
	remote_target.send(message.encode())

	# receive and print message
	response = remote_target.recv(1024).decode()
	print(response)

host_ip = '127.0.0.1'
host_port = 2222

listener_handler()