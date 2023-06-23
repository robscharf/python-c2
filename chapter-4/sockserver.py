import socket

def listener_handler():
	# bind websocket to host ip/port
	sock.bind((host_ip, host_port))
	print('[+] Awaiting connection from client...')
	
	# set socket to listen and accept connections from the address declared in app variables
	sock.listen()
	
	remote_target, remote_ip = sock.accept()
	# use {remote_ip[0]} to omit port from print statement
	print(f'[+] Connection received from {remote_ip}')

	# keep connection open via while loop
	while True:
		try:
			# capture and send message
			message = input('Message to send#> ')

			# exit message handling
			if message == 'exit':
				remote_target.send(message.encode())
				remote_target.close()
				break		

			remote_target.send(message.encode())
		
			# receive and print message
			response = remote_target.recv(1024).decode()
			if response == 'exit':
				print('[-] The client has terminated the session.')
				remote_target.close()
				break
			print(response)
		
		# Custom error/exit messages
		except KeyboardInterrupt:
			print("[~] Keyboard interrupt received.")
			remote_target.close()
			break

		except Exception:
			print("[~] Generic error message.")
			remote_target.close()
			break

# instantiate websocket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_ip = '127.0.0.1'
host_port = 2229

listener_handler()