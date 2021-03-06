# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 23:55:18 2018

@author: 陸
"""

from setting import field,BattleSystem
from makecard import card,follower,Amulet,Spell,BubetuNoSinja,makeCard,makeDeck,BattleDeck,BubetuNoEnsou,Aira,Filene,ServantOfDisdain,DragonOracle,VileVioletDragon,WatersOfTheOrca

def main():
    cardMaker = makeCard()
    Faiters = []
    for i in range(8):
        Faiters.append(WatersOfTheOrca())
        Faiters.append(DragonOracle())
        Faiters.append(cardMaker.makeFollower(name="Faiter"+str(i),cost=2,AP=2,HP=2))
        Faiters.append(Filene())
        Faiters.append(BubetuNoSinja())
     
    ghosts = []
    for i in range(10):
        ghosts.append(BubetuNoEnsou())
        ghosts.append(ServantOfDisdain())
        ghosts.append(Aira())
        ghosts.append(VileVioletDragon())
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

