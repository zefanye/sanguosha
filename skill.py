import card
import player
import hero
class skill:
    
    def __init__(self, sn, sty, st, sf, sd):
        self.skill_trigger=st
        self.skill_type=sty
        self.skill_frequency=sf
        self.skill_name=sn
        self.skill_description=sd
    
    
def show_skill(self, player=None):
    msg = self.skill_name+" "+self.skill_type+" "+self.skill_trigger+" "+self.skill_description
    if player != None:
        player.print(msg)
    else:
        print(msg)
skill_bank=[] 
def skill_storage(self):
    global skill_bank
    yinghun=skill_bank.append(skill("yinghun","basic","preparation stage","1 per stage","Yinghun: Once in each of own preparation stage, if you are unhealthy, you choose an option:\n1. Let another character draw 1 card and discard X cards.\n2. Let another character draw X cards and discard 1 card.(X is the number of health you are missing.)"))
    
    return skill_bank
def yinghun(self):
        global skill_bank
        # Following code needs to be fixed as input can only be taking from a player
        user_choice=int(input("Choose between the two options: "))
        if user_choice==1:
            card.draw_cards(self)
            for i in range(hero.life_limit-player.p.life):
                card.discard_card(self)
                       
        elif user_choice==2:
            for i in range(hero.life_limit-player.p.life):
                  card.draw_cards(self)
            card.discard_card(self)
