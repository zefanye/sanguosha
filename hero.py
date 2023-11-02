class hero:
    def __init__(self, life_limit):
        # Please define attributes of hero here.
        # For example, if a hero has a attribute of life_limit, then add following code:
        # self.life_limit = life_limit
        # and add life_limit as a parameter to __init__, optionally with a default value
        # __init(self, life_limit = 3)
        print()

    def show(self):
        # please show everything about a hero here, with print
        # for example: print("life limit is", self.life_limit)
        print()

def main():
    hero1 = hero(4)
    hero1.show()

if __name__ == "__main__":
    main()