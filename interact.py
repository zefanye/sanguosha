# python module to interact with human players
import re
import player
import skill
import stage
    
   
def ask_player_action(p,current_stage,stage_commands):
    f=""
    for i in stage_commands:
        f+=i[0]
        if i!=stage_commands[len(stage_commands)-1]:
            f+=", "
#    for i in stage_commands:
#        if i != stage_commands[0]:
#            f+=", "
#        f+=i[0]   
    command=input("\nPlease pick action("+f+"): ")
    
    return interpret_command(p, command, current_stage)



def def_command(name, func):
    global all_commands
    all_commands.append([name, func])

def remove_empty_str(list):
    new_list=[]
    for i in list:
        if i!="":
            new_list.append(i)
    #print(new_list)
    return new_list

def interpret_command(p, str, current_stage):
    stage_commands=valid_commands(current_stage)
    arg_list=re.split(' ', str)
    new_arg_list = remove_empty_str(arg_list)
    return execute_command(p, new_arg_list[0], stage_commands, current_stage, new_arg_list)

def valid_commands(current_stage):
    stage_commands=all_commands.copy()
    if current_stage==stage.PREPARATION_STAGE:
        del stage_commands[6]
        del stage_commands[5]
        del stage_commands[4]
        del stage_commands[1]
        
        
        
    elif current_stage==stage.DETETMINATION_STAGE:
        del stage_commands[6]
        del stage_commands[5]
        del stage_commands[1]
        
    elif current_stage==stage.DRAW_STAGE:
        del stage_commands[6]
        del stage_commands[5]
        del stage_commands[4]   
        del stage_commands[1]
        
    
    elif current_stage==stage.PLAY_CARD_STAGE:
        del stage_commands[6]
        del stage_commands[5]
        del stage_commands[4]
        
        
    elif current_stage==stage.DISCARD_CARD_STAGE:
        del stage_commands[5]
        del stage_commands[4]
        del stage_commands[1]
       
    elif current_stage==stage.END_STAGE:
        del stage_commands[6]
        del stage_commands[5]
        del stage_commands[4]
        del stage_commands[1]
    return stage_commands    
def execute_command(p, str, stage_commands, *args ):
    valid=False
    
        
        
    for c in stage_commands:
        if (str == c[0]):
            valid=True
            return c[1](p, *args)
    if not valid:
        print(f"Unrecoginized command {str}")
        return 1

def end_play_stage(p, *args):
    return 0

def determine_card(p, *args):
    pass
def Discard_card(p, *args):
    pass

def Draw_card(p, *args):
    pass
def use_skill(p,*args):
    skill_use=input("Enter the name of the skill you want to use: ")
    for p in skill.skill_storage(p):
        #print(p.skill_name)
        if p.skill_name==skill_use:
            skill.show_skill(p)
            #skill.skill_effect(p)
def Show_part(p):
    print(p.id+" has "+str(len(p.cards))+" cards")
    Show_life(p)
    Show_hero(p)

def Show_cards(p):
    p.show_cards()
    
def Show_life(p):
    p.show_life()

def Show_hero(p):
    p.show_hero()

def Show_role(p):
    p.show_role()

def Show_all(p,*args):
    Show_cards(p)
    Show_life(p)
    Show_hero(p)
    Show_role(p)
    print("\n")


def play_card(p, *args):
    
    action=int(input("Play which card: "))
    action=action-1
    p.play_card(action)

all_commands=[]
def_command("end", end_play_stage)
def_command("play", play_card)
def_command("skill", use_skill)
def_command("show",Show_all)
def_command("determine",determine_card)
def_command("draw",Draw_card)
def_command("discard",Discard_card)