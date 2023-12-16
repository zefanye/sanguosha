# python module to interact with human players

def def_command(name, func):
    global all_commands
    all_commands.append([name, func])

def interpret_command(str):
    
    pass

def execute_command(str, *args):
    valid=False
    for c in all_commands:
        if (str == c[0]):
            valid=True
            c[1](*args)
            break
    if not valid:
        print(f"Unrecoginized command {str}")

all_commands=[]