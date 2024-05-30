import socket
import sys
import threading
import re
import time
import card
import hero
import interact
import global_var
import player
import stage

address = socket.gethostname()
port = 2008
max_num_clients = 2
num_connection = 0
server_threads=[]

# a simple protocol between server and client
# Direction: server to client

# All server to client commands should start with:
start_mark = "!"

# Then followed by a number to discribe length of data

# Then followed by a separator between length and command
end_len_mark = " "

# Then followed by a command

# When server asks the client to collect input, the prompt should be
# prefixed with "INPUT ". Say: "INPUT Please pick a card to play".
# The client will show the promot, collect input from user and send
# back to the server. The message sent back should be prefixed with collected_prefix
input_command="INPUT"

# Direction: server to client
# When the server asks the client to just show a message, the message
# should be prefixed with "!PRINT ". Say: "!PRINT Your turn has ended.
# Please wait for other players' turn". The client will just print the message.
print_command="PRINT"

quit_command="QUIT"

# Then followed by a end of command separator:
end_mark="!"

# Finally by length of data

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
    # initialize card stack, hero list and roles
    card.init()
    # TODO: initialize hero list and roles
    # Now it is ready to notify players to pick role/hero and initial cards
    for t, conn, (event_ready_to_start, event_player_ready) in server_threads:
        event_ready_to_start.set()

    # Wait for all players to finish picking role/hero and cards
    for t, conn, (event_ready_to_start, event_player_ready) in server_threads:
        event_player_ready.wait()

    try:
        # Now all players are ready to play stages. Get the list of all players now
        all_players=global_var.get_live_players()
        live_players = all_players
        while (len(live_players) > 1):
            for p in live_players:
                if p.life > 0:
                    stage.round(p)
            live_players = global_var.get_live_players_from(all_players)

        # The only remaining player is the winner
        live_players[0].print("You win! Congratulations.")
    finally:
        for t, conn, (event_ready_to_start, event_player_ready) in server_threads:
          conn.send(f"{start_mark}{0}{end_len_mark}{quit_command}{end_mark}".encode())
        for t, conn, (event_ready_to_start, event_player_ready) in server_threads:
          t.join()
          conn.close()
        print("Server is down")

def print_to_remote(conn, msg):
    m = f"{start_mark}{len(msg)}{end_len_mark}{print_command}{end_mark}{msg}"
    conn.send(m.encode())

def input_from_remote(conn, msg):
    m = f"{start_mark}{len(msg)}{end_len_mark}{input_command}{end_mark}{msg}"
    conn.send(m.encode())
    return conn.recv(1024).decode()

def player_thread(events, player_id, conn, address):
    event_ready_to_start, event_player_ready = events
    print_to_remote(conn, "waiting for all players to connect ...")
    event_ready_to_start.wait()
    print_to_remote(conn, f"All players connected. Number of players is {num_connection}. My player id is {player_id}")
    if player_id == 0:
        p = player.player(f"player{player_id}","monarch",cards=[], hero=hero.hero1,life=4+1,life_limit=4+1, remote_connection=conn)
        for i in range(5):
            p.draw_cards()
    else:
        p = player.player(f"player{player_id}","rebellion",cards=[], hero=hero.hero2, life=3,life_limit=3, remote_connection=conn)
        for i in range(5):
            p.draw_cards()
    global_var.add_live_player(p)
    p.status()
    p.show_cards()
    # wait for all users to connect
    # Allocate role
    # choose a hero
    # create player with avaliable info
    # wait until game completed
    # print_to_remote(conn, f"Wait for game to complete...")
    event_player_ready.set()

if __name__ == "__main__":
    start_server(address, port)

