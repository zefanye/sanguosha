
class card:
    def __init__(self, cat, s, n, na, ec="", r="", tc="", e="", d="", i=""):
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
        
            
        print("This is card:", element_str+self.name, self.suit, self.number, tc_str+self.category+equipment_category_str, self.description, self.image)

def main():

    #card1=card("basic","hearts","9","peach")
    #card2=card("tips","spades","A","lightning")

    all_cards=[]




    all_cards.append(card("equipment","spades","K","da_wuan","-1 horse"))
    all_cards.append(card("tips","spades","J","steal"))
    all_cards.append(card("basic","spades","5","attack",e="thunder"))
    all_cards.append(card("tips","spades","A","lightning",tc="delayed"))
    all_cards.append(card("basic","hearts","2","dodge"))
    all_cards.append(card("basic","hearts","9","peach"))
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
    all_cards.append(card("equipment","spades","5","due ying","+1 horse"))
    all_cards.append(card("tips","hearts","9","something from nothing"))
    all_cards.append(card("tips","spades","3","steal"))
    all_cards.append(card("equipment","spades","2","masculine feminine double wielded swords"))
    all_cards.append(card("basic","hearts","6","peach"))
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
    all_cards.append(card("basic","spades","8","attack"))
    all_cards.append(card("basic","spades","8","attack"))
    all_cards.append(card("basic","spades","8","attack"))
    all_cards.append(card("basic","spades","8","attack"))
    all_cards.append(card("basic","spades","8","attack"))


    for c in all_cards:
        c.show()

if __name__ == "__main__":
    main()