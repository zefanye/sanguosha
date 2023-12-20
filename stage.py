# define stages
# determination stage
# picking card stage
# playing card stage
# discarding card stage
import interact
import player

def preparation_stage(p):
    print("\n"+p.id+"'s turn: " )
    print("preparation_stage")
    
def determination_stage(p):
    print("determination_stage")

def pick_card_stage(p):
    for i in range(2):
        p.draw_cards()
    print("pick_card_stage")
    # Player draw two cards
    

def play_card_stage(p):
    print("in playing card")
    while (interact.ask_player_action(p) != 0):
        pass

def discard_card_stage(p):
    print("discard_card_stage")

def end_stage(p):
    print("end_stage")

def round(p):
    preparation_stage(p)
    determination_stage(p)
    pick_card_stage(p)
    play_card_stage(p)
    discard_card_stage(p)
    end_stage(p)
