import player

def action_default(self_card, player):
    print("This is the default action for")
    self_card.show()
    return True
    
class card:
    def __init__(self, cat, s, n, na, ec="", r="", tc="", e="", d="", i="", action=action_default):
        self.category=cat
        self.suit=s
        self.number=n
        self.name=na
        self.description=d
        self.image=i
        self.element=e
        self.equipment_category=ec
        self.range=r
        self.tips_category=tc
        self.action=action
        
    def show(self):
        element_str =""
        if self.element != "":
            element_str=self.element+"-"
        
        equipment_category_str=""
        if self.equipment_category != "":
            equipment_category_str="("+self.equipment_category
            if self.equipment_category=="weapons":
                equipment_category_str += self.range
            equipment_category_str += ")"
        tc_str=""
        if self.tips_category !="":
            tc_str=self.tips_category+"-"
        
            
        print("This is card:", element_str+self.name, "["+self.suit, self.number, tc_str+self.category+equipment_category_str, self.description, self.image+"]")
    def play(self, self_player:player):
        #if self.name=="something from nothing":
        #    print("Play something from nothing")
        #    for i in range(2):
        #        self_player.draw_cards()
        return self.action(self, self_player)

def shuffle(cards_to_shuffle):
    import random
    copied_cards=cards_to_shuffle.copy()
    s=[]
    
    #print(len(cards_to_shuffle))
    for i in range(len(copied_cards)):
        randomCards=random.randint(0,len(copied_cards)-1)
        #print(randomCards)
        s.append(copied_cards[randomCards])
        del copied_cards[randomCards]
    return s

##############################################
# Define all card actions here
# All card actions must accept two parameters:
#   self_card: the card that has the action
#   player: the player who play the card
def action_something_from_nothing(self_card, player):
    for i in range(2):
        player.draw_cards()
    return True

def action_peach(self_card, player):
   
    succesful=player.restore_health()
    return succesful
def add_all_cards():

    #card1=card("basic","hearts","9","peach")
    #card2=card("tips","spades","A","lightning")

    global all_cards
    all_cards.append(card("equipment","spades","K","da_wuan","-1 horse"))
    all_cards.append(card("tips","spades","J","steal"))
    all_cards.append(card("basic","spades","5","attack",e="thunder"))
    all_cards.append(card("tips","spades","A","lightning",tc="delayed"))
    all_cards.append(card("basic","hearts","2","dodge"))
    all_cards.append(card("basic","hearts","9","peach", action=action_peach))
    all_cards.append(card("equipment","diamonds","A","fan","weapons","4"))
    all_cards.append(card("tips","clubs","Q","unbreakable")) 
    all_cards.append(card("equipment","spades","5","dragon blade","weapons","3"))
    all_cards.append(card("tips","spades","7","barbarian invasion"))
    all_cards.append(card("equipment","heart","5","red rabbit","-1 horse" ))
    all_cards.append(card("basic","diamonds","7","dodge"))
    all_cards.append(card("tips","spades","K","barbarian invasion"))
    all_cards.append(card("basic","clubs","8","attack"))
    all_cards.append(card("equipment","hearts","5","kirin bow","weapons","5"))
    all_cards.append(card("basic","diamonds","2","dodge"))
    all_cards.append(card("tips","hearts","A","brotherhood"))
    all_cards.append(card("equipment","spades","5","jue ying","+1 horse"))
    all_cards.append(card("tips","hearts","9","something from nothing", action=action_something_from_nothing))
    all_cards.append(card("tips","spades","3","steal"))
    all_cards.append(card("equipment","spades","2","masculine feminine double wielded swords","weapons","2"))
    all_cards.append(card("basic","hearts","6","peach", action=action_peach))
    all_cards.append(card("basic","hearts","10","attack"))
    all_cards.append(card("tips","diamonds","3","steal"))
    all_cards.append(card("basic","diamonds","6","dodge"))
    all_cards.append(card("basic","hearts","2","dodge"))
    all_cards.append(card("tips","clubs","Q","unbreakable"))
    all_cards.append(card("tips","clubs","A","duel"))
    all_cards.append(card("basic","diamonds","K","attack"))
    all_cards.append(card("tips","spades","6","enprisoned"))
    all_cards.append(card("equipment","clubs","A","silver lion helmet"))
    all_cards.append(card("basic","spades","3","wine"))
    all_cards.append(card("basic","diamonds","7","dodge"))
    all_cards.append(card("equipment","diamonds","K","hua liu"))
    all_cards.append(card("basic","hearts","9","peach", action=action_peach))
    all_cards.append(card("basic","clubs","8","attack"))
    all_cards.append(card("basic","diamonds","9","attack"))
    all_cards.append(card("basic","diamonds","Q","peach", action=action_peach))
    all_cards.append(card("tips","clubs","4","discard"))
    all_cards.append(card("basic","clubs","J","attack"))
    all_cards.append(card("basic","spades","7","attack"))
    all_cards.append(card("tips","clubs","Q","borrow weapon"))
    all_cards.append(card("tips","hearts","4","harvest"))
    all_cards.append(card("basic","hearts","2","dodge"))
    all_cards.append(card("basic","diamonds","J","dodge"))
    all_cards.append(card("basic","hearts","4","attack",e="fire"))
    all_cards.append(card("tips","hearts","9","something from nothing"))
    all_cards.append(card("tips","spades","3","discard"))
    all_cards.append(card("equipment","diamonds","Q","attack"))
    all_cards.append(card("tips","hearts","Q","discard"))
    all_cards.append(card("tips","diamonds","Q","fire attack"))
    all_cards.append(card("basic","diamonds","Q","peach", action=action_peach))
    all_cards.append(card("tips","diamonds","Q","unbreakable"))
    all_cards.append(card("basic","diamonds","K","attack"))
    all_cards.append(card("equipment","diamonds","K","purple_horse","-1 horse"))
    all_cards.append(card("equipment","diamonds","A","zhuge_crossbow","weapons","1"))
    all_cards.append(card("basic","diamonds","2","dodge"))
    all_cards.append(card("equipment","spades","2","bagua_array"))
    all_cards.append(card("basic","diamonds","2","peach", action=action_peach))
    all_cards.append(card("equipment","clubs","2","bagua_array"))
    all_cards.append(card("equipment","spades","6","qing_gang_sword","weapons","2"))
    all_cards.append(card("basic","hearts","J","dodge"))
    all_cards.append(card("basic","diamonds","2","peach", action=action_peach))
    return

all_cards = []

card_stack = []

discard_pile=all_cards
 


def extract_card_from_stack(): 
    global card_stack
    global discard_pile
    if len(card_stack)==0:
        card_stack=shuffle(discard_pile)
        discard_pile=[]
        # discard_pile need to be emptied here!!!   
    cards=card_stack[0]
    del card_stack[0]
    return cards

def discard_card(c):
    global discard_pile
    discard_pile.append(c)




def card_type_bank():
    pass

def init():
    add_all_cards()
    global card_stack
    card_stack = shuffle(all_cards)
    card_stack.insert(0, card("basic","diamonds","2","peach", action=action_peach))
    #for c in card_stack:
    #    c.show()

def main():
    init()
    for i in range(100):
        c = extract_card_from_stack()
        c.show()
        discard_card(c)

if __name__ == "__main__":
    main()