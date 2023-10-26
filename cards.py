
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


for c in all_cards:
    c.show()
