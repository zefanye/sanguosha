live_players=[]
default_port=2008

def set_live_players(all_players):
    global live_players
    live_players=all_players

def get_live_players():
    global live_players
    return live_players