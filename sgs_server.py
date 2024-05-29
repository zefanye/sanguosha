import socket
import sys
import threading
import re
import time
import interact

address = socket.gethostname()
port = 2008
max_num_clients = 2
num_connection = 0
server_threads=[]

# a simple protocol between server and client

# Direction: server to client
# When server asks the client to collect input, the prompt should be
# prefixed with "!INPUT ". Say: "!INPUT Please pick a card to play".
# The client will show the promot, collect input from user and send
# back to the server. The message sent back should be prefixed with collected_prefix
input_prefix="!INPUT "

# Direction: server to client
# When the server asks the client to just show a message, the message
# should be prefixed with "!PRINT ". Say: "!PRINT Your turn has ended.
# Please wait for other players' turn". The client will just print the message.
print_prefix="!PRINT "

quit_command="!QUIT"

''' invalid
# Direction: client to server
# When the client sends data back to the server, the data should be
# prefixed with "!COLLECTED "
# collected_prefix="!DATA "
'''
def start_server(host, port):
    global num_connection
    print(host, port)
    server_socket = socket.socket()  # get instance
    #server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # Set timeout and time stamp
    # timeout = 1 makes the waiting loop to check every 1 second
    # timestamp = 120 makes the waiting loop complete in 2 minutes. If no
    # more connection is coming in 2 minutes, stop accepting new connections
    server_socket.settimeout(1)
    timestamp = 120

    # configure how many client the server can listen simultaneously
    server_socket.listen(max_num_clients)

    while timestamp > 0 and num_connection < max_num_clients:
      try: 
        conn, address = server_socket.accept() 
      except socket.timeout:
        print(f"Time remaining to connect: {timestamp}s")
        timestamp -= 1
        pass
      except:
        raise
      else:
        print("Connection from: " + str(address))
        events = [threading.Event() for i in range(2)]
        t = threading.Thread(target=player_thread, args=[events, num_connection, conn, address])
        server_threads.append((t, conn, events))
        t.start()
        num_connection += 1
    print(f"Finished waiting for connection. Number of connection accepted is {num_connection}")
    for t, conn, events in server_threads:
        events[0].set()
    time.sleep(10)
    for t, conn, events in server_threads:
        conn.send(quit_command.encode())
    for t, conn, events in server_threads:
        events[1].set()
    for t, conn, events in server_threads:
        t.join()
        conn.close()
    print("Server is down")

def print_to_player(conn, msg):
    msg = f"{print_prefix}{len(msg)}!{msg}\n"
    conn.send(msg.encode())

def player_thread(events, player_id, conn, address):
    event_ready_to_start, event_game_complete = events
    print_to_player(conn, "waiting for all players to connect ...")
    event_ready_to_start.wait()
    print_to_player(conn, f"All players connected. Number of players is {num_connection}. My player id is {player_id}")
    # wait for all users to connect
    # Allocate role
    # choose a hero
    # create player with avaliable info
    # wait until game completed
    print_to_player(conn, f"Wait for game to complete...")
    event_game_complete.wait()

if __name__ == "__main__":
    start_server(address, port)

