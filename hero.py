class hero:
    def __init__(self, life_limit,current_health,nation,name):
        # Please define attributes of hero here.
        # For example, if a hero has a attribute of life_limit, then add following code:
        self.life_limit = life_limit
        # and add life_limit as a parameter to __init__, optionally with a default value
        # __init__(self, life_limit = 3)
        self.current_health=current_health
        self.nation=nation
        self.name=name

    def show(self, player=None):
        # please show everything about a hero here, with print
        # for example: print("life limit is", self.life_limit)
        msg = str(self.life_limit) +" "+ str(self.current_health)+" "+self.nation+" "+self.name
        if player != None:
            player.print(msg)
        else:
            print(msg)
    
hero1 = hero(4,4,"shu","zhaoyun")
hero2=hero(4,4,"wu","sunjian")
def main():
    hero1.show()
    hero2.show()
if __name__ == "__main__":
    main()