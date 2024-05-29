import socket
import re
import sgs_server

def start_client(host, port):
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    while True:
        command = client_socket.recv(1024).decode()
        explain_command = re.match(sgs_server.input_prefix+"(.*)", command)
        if explain_command:
            prompt = explain_command.groups()[0]
            data = input(prompt)
            client_socket.send(data.encode())
        explain_command = re.match(sgs_server.print_prefix+"(.*)", command)
        if explain_command:
            msg = explain_command.groups()[0]
            print(msg)
    '''
    message = input(" -> ")  # take input
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal
        message = input(" -> ")  # again take input
    '''
    client_socket.close()  # close the connection

start_client()
