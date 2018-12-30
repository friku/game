# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 23:55:18 2018

@author: 陸
"""

from setting import field,BattleSystem
from makecard import card,follower,Amulet,Spell,BubetuNoSinja,makeCard,makeDeck,BattleDeck

def main():
    cardMaker = makeCard()
    Faiters = []
    for i in range(40):
        Faiters.append(cardMaker.makeFollower(name="Faiter"+str(i),cost=2,AP=2,HP=2))
     
    ghosts = []
    for i in range(40):
        ghosts.append(BubetuNoSinja())
#        ghosts.append(cardMaker.makeFollower(name="ghost"+str(i),cost=1,AP=1,HP=1))
    
    BTDeck = BattleDeck(Faiters)
    BTGDeck = BattleDeck(ghosts)
    print(BTDeck.deck[0].name)
    print("Got Deck")
    print(BTGDeck.deck[0].name)
    print("Got GDeck")
    
    BTSystem = BattleSystem()
    BTSystem.BattlePreparation(BTDeck,BTGDeck)
    print(BTSystem.Field[0].playerName)
    BTSystem.turn(0)
    print("main result")
    return True
    
    
    
    


if __name__ == '__main__':
    main()

