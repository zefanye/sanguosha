import card
import hero
import player
import stage

def main():
    card.card.init()    
    p1 = player("player1","monarch",hero=hero.hero1,life=4)
    for i in range(5): 
        p1.draw_cards()
    #p1.show_cards()
    p2 = player("player2","rebellion",hero=hero.hero2, life=3) 
    for i in range(5): 
        p2.draw_cards()
    #p2.show_cards()
    all_players=[p1, p2]
    live_players=all_players

    while (len(live_players) > 1):
        for p in live_players:
            stage.round(p)
        live_players = get_live_players_from(all_players)

if __name__ == "__main__":
    main()