import card
import hero

class player:
    def __init__(self, id, role, cards = [], hero = None, life = 0):
        self.id = id
        self.cards = cards
        self.life = life
        self.hero = hero
        self.role = role

    def status(self):
        print(f"Player {self.id}: hero {self.hero.name}, life {self.life}")
        print(f"Hero's life limit {self.hero.life_limit}")

    def disclose_role(self):
        print(f"Player {self.id}''s role is {self.role}")
        print("Player", self.id, "''s role is ", self.role)
    
    def draw_cards(self):
        self.cards.append(card.extract_card_from_stack())
        
    
    def show_cards(self):
        print(self.id+" has "+str(len(self.cards))+" cards")
        for c in self.cards:
            c.show()

    def show_life(self):
        print(self.id+" has "  +str(self.life)+" life")
    
    def show_hero(self):
        print(self.id+" is playing as "+self.hero.name)

    def show_role(self):
        print(self.id+" is a "+self.role)
    
    def play_card(self,index):
        current_card=self.cards[index]
        success=current_card.play(self)
        if success:
            del self.cards[index]

def main():

    card.init()    
    p1 = player("player1","monarch",hero=hero.hero1,life=4)
    for i in range(5): 
        p1.draw_cards()
    p1.show_cards()
    #p2 = player("player2","zuoci","rebellion",life=3) 
    p1.status()


if __name__ == "__main__":
    main()

    