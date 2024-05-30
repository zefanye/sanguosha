import socket
import re
import sys
import sgs_server

def receive_command(socket):
    command = ""
    state = "BEGIN"
    data_len = 0
    received_len = 0
    i = 0
    while True:
        char = socket.recv(1).decode()
        if not char:
            break
        if state == "BEGIN":
            if char != sgs_server.start_mark:
                print(f"Warning: unrecognized start of command: {char}")
            else:
                state = "LENGTH"
                len_buff = ""
            continue
        if state == "LENGTH":
            if char.isnumeric():
                len_buff += char
            elif char == sgs_server.end_len_mark:
                data_len = int(len_buff)
                state = "COMMAND"
                command_buff = ""
            else:
                print(f"Warning: unexpected char encountered when looking for len: {char}")
            continue
        if state == "COMMAND":
            if char.isalpha():
                command_buff += char
            elif char == sgs_server.end_mark:
                state = "DATA"
                data_buff = ""
                received_len = 0
                if received_len >= data_len:
                    break
            continue
        if state == "DATA":
            data_buff += char
            received_len += 1
            if received_len >= data_len:
                break
            else:
                continue
    return (command_buff, data_buff)

def start_client(host, port):
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    while True:
        command, data = receive_command(client_socket)
        if not command:
            # if data is not received break
            break
        if command == sgs_server.input_command:
            user_input = input(data)
            client_socket.send(user_input.encode())
            continue
        if command == sgs_server.print_command:
            print(data)
            continue
        if command == sgs_server.quit_command:
            print("Bye! Server side ends the game.")
            break
        print(f"Warning: Unrecoginized command: {command}: {data}")
    client_socket.close()  # close the connection

if __name__ == "__main__":
    if len(sys.argv) > 1:
        start_client(sys.argv[1], sgs_server.port)
    else:
        start_client(socket.gethostname(), sgs_server.port)
