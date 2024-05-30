import card
import hero
import sgs_server

class player:
    def __init__(self, id, role, cards = [], hero = None, life = 0, life_limit=0, remote_connection=None):
        self.id = id
        self.cards = cards
        self.life = life
        self.hero = hero
        self.role = role
        self.life_limit=life_limit
        self.remote_connection = remote_connection

    def status(self):
        self.print(f"Player {self.id}: hero {self.hero.name}, life {self.life}, life_limit {self.life_limit}")
        self.print(f"Hero's life limit {self.hero.life_limit}")

    def disclose_role(self):
        self.print(f"Player {self.id}''s role is {self.role}")
     
    def restore_health(self):
        if self.life<self.life_limit:
            self.life=self.life+1
            return True
        return False
    def draw_cards(self):
        self.cards.append(card.extract_card_from_stack())
        
    def play_dodge(self):
        have_dodge=False
        for i in self.cards:
            if i.name=="dodge":
                have_dodge=True
                break
        if have_dodge:
            play=self.input("Do you want to play a dodge? ")
            if play=="yes":
                which_dodge=int(self.input("Which dodge card do you want to play? "))
                playdodge=self.cards[which_dodge]
                if playdodge.name=="dodge":
                    self.discard_card()
        succesful=False
        return succesful
    def show_cards(self):
        self.print(self.id+" has "+str(len(self.cards))+" cards")
        for c in self.cards:
            c.show(self)

    def show_life(self):
        self.print(self.id+" has "  +str(self.life)+" life")
    
    def show_hero(self):
        self.print(self.id+" is playing as "+self.hero.name)

    def show_role(self):
        self.print(self.id+" is a "+self.role)
    
    def play_card(self,index):
        current_card=self.cards[index]
        success=current_card.play(self)
        if success:
            del self.cards[index]
        else:
            self.print("cannot play this card")

    # Get input from this player
    def input(self, prompt):
        if not self.remote_connection:
            # call the system input
            return input(prompt)
        else:
            return sgs_server.input_from_remote(self.remote_connection, prompt)

    # Print standard output to this player
    def print(self, msg):
        if not self.remote_connection:
            # call the system print
            print(msg)
        else:
            return sgs_server.print_to_remote(self.remote_connection, msg)

def main():

    card.init()    
    p1 = player("player1","monarch",hero=hero.hero1,life=4,life_limit=4)
    for i in range(5): 
        p1.draw_cards()
    p1.show_cards()
    #p2 = player("player2","zuoci","rebellion",life=3) 
    p1.status()


if __name__ == "__main__":
    main()

    