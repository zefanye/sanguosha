import card
import hero
import player
import stage

def get_live_players_from(ap):
    lp=[]
    #if ap[0].life>0:
    #    lp.append(ap[0])
    #if ap[1].life>0:
    #    lp.append(ap[1])
    for p in ap:
        if p.life>0:
            lp.append(p)     
         
         #or ap[1].life<=0:
    return lp
        
    


def main():
    card.init()    
    p1 = player.player("player1","monarch",cards=[], hero=hero.hero1,life=4+1)
    for i in range(5): 
        p1.draw_cards()
    #p1.show_cards()
    p2 = player.player("player2","rebellion",cards=[], hero=hero.hero2, life=3)
    #p2.show_cards()
    for i in range(5): 
        p2.draw_cards()
    #p2.show_cards()
    all_players=[p1, p2]
    live_players=all_players

    while (len(live_players) > 1):
        for p in live_players:
            if p.life > 0:
                stage.round(p)
        live_players = get_live_players_from(all_players)

if __name__ == "__main__":
    main()