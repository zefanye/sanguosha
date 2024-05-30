from threading import Lock

live_players=[]
live_player_lock=Lock()

def set_live_players(all_players):
    global live_players
    live_players=all_players

def get_live_players():
    global live_players
    return live_players

def add_live_player(p):
    global live_players
    with live_player_lock:
        live_players.append(p)

def get_live_players_from(ap):
    lp=[]
    for p in ap:
        if p.life>0:
            lp.append(p)
    return lp
