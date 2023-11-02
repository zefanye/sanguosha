import cards

class player:
    def __init__(self, id, role, cards = [], hero = None, life = 0):
        self.id = id
        self.cards = cards
        self.life = life
        self.hero = hero
        self.role = role

    def status(self):
        print(f"Player {self.id}: hero {self.hero}, life {self.life}")

    def disclose_role(self):
        print(f"Player {self.id}''s role is {self.role}")


def main():
    p1 = player("player1", "king")
    p1.status()

if __name__ == "__main__":
    main()

    