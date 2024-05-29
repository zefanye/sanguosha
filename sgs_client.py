import socket
import re
import sys
import sgs_server

def start_client(host, port):
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    quit = False
    while not quit:
        commands = client_socket.recv(1024).decode()
        if not commands:
            # if data is not received break
            break
        for command in re.split('\n', commands):
            explain_command = re.match(sgs_server.input_prefix+"(\d+)!(.*)", command)
            if explain_command:
                prompt = explain_command.groups()[1]
                data_len = int(explain_command.groups()[0])
                if (data_len != len(prompt)):
                    print(f"Warning: received data length mis-match {data_len} vs. {len(prompt)}")
                data = input(prompt)
                client_socket.send(data.encode())
                continue
            explain_command = re.match(sgs_server.print_prefix+"(\d+)!(.*)", command)
            if explain_command:
                msg = explain_command.groups()[1]
                data_len = int(explain_command.groups()[0])
                if (data_len != len(msg)):
                    print(f"Warning: received data length mis-match {data_len} vs. {len(msg)}")
                print(msg)
                continue
            explain_command = re.match(sgs_server.quit_command, command)
            if explain_command:
                quit = True
                break
    client_socket.close()  # close the connection

if __name__ == "__main__":
    if len(sys.argv) > 1:
        start_client(sys.argv[1], sgs_server.port)
    else:
        start_client(socket.gethostname(), sgs_server.port)
