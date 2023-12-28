# python module to interact with human players
import re
import player
def ask_player_action(p):
    command = input("Please pick action: ")
    return interpret_command(p, command)

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

def interpret_command(p, str):
    arg_list=re.split(' ', str)
    new_arg_list = remove_empty_str(arg_list)
    return execute_command(p, new_arg_list[0], new_arg_list)

def execute_command(p, str, *args):
    valid=False
    for c in all_commands:
        if (str == c[0]):
            valid=True
            return c[1](p, *args)
    if not valid:
        print(f"Unrecoginized command {str}")
        return 1

def end_play_stage(p, *args):
    return 0

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
    print(args)
    return 1

all_commands=[]
def_command("end", end_play_stage)
def_command("play", play_card)
def_command("show",Show_all)