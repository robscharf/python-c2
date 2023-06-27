import socket
import sys

def comm_in(remote_target):
	print('[+] Awaiting response...')
	response = remote_target.recv(1024).decode()
	return response

def comm_out(remote_target, message):  
	remote_target.send(message.encode())

def listener_handler():  
	sock.bind((host_ip, host_port))  
	print('[+] Awaiting connection from client...')  
	sock.listen()  
	remote_target, remote_ip = sock.accept()  
	comm_handler(remote_target, remote_ip)

def comm_handler(remote_target, remote_ip):  
	print(f'[+] Connection received from {remote_ip[0]}')  
	while True:  
		try:  
			message = input('Command -> ')  
			if message == 'exit':  
				remote_target.send(message.encode())  
				remote_target.close()
				break
			remote_target.send(message.encode())  
			response = remote_target.recv(1024).decode()  
			if response == 'exit':  
				print('[-] The client has terminated the session.')  
				remote_target.close()  
				break  
			print(response)  
		except KeyboardInterrupt:  
			print('[+] Keyboard interrupt issued.')  
			remote_target.close()  
			break  
		except Exception:  
			remote_target.close()  
			break			

def banner():
	print("            __                                  _                 __       _                                      ____   ")
	print("   _ ___    LJ    ___ _     ____      ____     FJ___      ____    LJ    ___FJ     ____     _ ___        ____     / _  `. ")
	print("  J '__ J   FJ   F __` L   F ___J.   F __ J   J  __ `.   F __ J   FJ   F __  L   F __ J   J '__ \",     F ___J.  J_/-7 .' ")
	print("  | |--| | J  L | |--| |  | |---LJ  | _____J  | |--| |  | |--| | J  L | |--| |  | _____J  | |__|-J    | |---LJ  `-:'.'.' ")
	print("  F L__J J J  L F L__J J  F L___--. F L___--. F L  J J  F L__J J J  L F L__J J  F L___--. F L  `-'    F L___--. .' ;_J__ ")
	print(" J  _____/LJ__LJ\____,__LJ\______/FJ\______/FJ__L  J__LJ\______/FJ__LJ\____,__LJ\______/FJ__L        J\______/FJ________L")
	print(" |_J_____F |__| J____,__F J______F  J______F |__L  J__| J______F |__| J____,__F J______F |__L         J______F |________|")
	print(" L_J                                                                                                                     ")




if __name__ == '__main__':
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	host_ip = sys.argv[1]  
	host_port = int(sys.argv[2])

	banner()
	listener_handler()

