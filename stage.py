# define stages
# determination stage
# picking card stage
# playing card stage
# discarding card stage
import interact
import player
import global_var
def preparation_stage(p):
    live_players=global_var.get_value()
    print("\n"+p.id+"'s turn: " )
    print("preparation_stage")
    interact.Show_all(p)
    
    for p_other in live_players:
        if p_other!=p:
            if p_other.life > 0:
                interact.Show_part(p_other)
    interact.interpret_stage(p)
    while (interact.ask_player_action(p) != 0):
        pass
    #interact.Show_part(p)
def determination_stage(p):
    print("determination_stage")

def draw_stage(p):
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
    draw_stage(p)
    play_card_stage(p)
    discard_card_stage(p)
    end_stage(p)
