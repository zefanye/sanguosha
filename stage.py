# define stages
# determination stage
# picking card stage
# playing card stage
# discarding card stage
import interact
import player
import global_var


PREPARATION_STAGE=1
DETETMINATION_STAGE=2
DRAW_STAGE=3
PLAY_CARD_STAGE=4
DISCARD_CARD_STAGE=5
END_STAGE=6
#determinationstage=2
#draw stage=3
#play card stage=4
#discard card stage=5
#end stage=6
def preparation_stage(p):
    current_stage=PREPARATION_STAGE
    stage_commands=interact.valid_commands(current_stage)
    live_players=global_var.get_value()
    p.print("\n"+p.id+"'s turn: " )
    p.print("preparation_stage")
    interact.Show_all(p)
    
    for p_other in live_players:
        if p_other!=p:
            if p_other.life > 0:
                interact.Show_part(p_other)
    #interact.interpret_stage(p)
    while (interact.ask_player_action(p, current_stage,stage_commands) != 0):
        pass
        
    #interact.Show_part(p)
def determination_stage(p):
    current_stage=DETETMINATION_STAGE
    stage_commands=interact.valid_commands(current_stage)
    p.print("determination_stage")
    while (interact.ask_player_action(p, current_stage,stage_commands) != 0):
        pass
def draw_stage(p):
    current_stage=DRAW_STAGE
    stage_commands=interact.valid_commands(current_stage)
    for i in range(2):
        p.draw_cards()
    # Player draw two cards
    while (interact.ask_player_action(p, current_stage,stage_commands) != 0):
        pass

def play_card_stage(p):
    current_stage=PLAY_CARD_STAGE
    stage_commands=interact.valid_commands(current_stage)
    p.print("in playing card")
    while (interact.ask_player_action(p, current_stage,stage_commands) != 0):
        pass

def discard_card_stage(p):
    current_stage=DISCARD_CARD_STAGE
    stage_commands=interact.valid_commands(current_stage)
    p.print("discard_card_stage")
    while (interact.ask_player_action(p, current_stage,stage_commands) != 0):
        pass

def end_stage(p):
    current_stage=END_STAGE
    stage_commands=interact.valid_commands(current_stage)
    p.print("end_stage")
    while (interact.ask_player_action(p, current_stage,stage_commands) != 0):
        pass
def round(p):
    preparation_stage(p)
    determination_stage(p)
    draw_stage(p)
    play_card_stage(p)
    discard_card_stage(p)
    end_stage(p)
