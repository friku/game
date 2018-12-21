# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 23:55:18 2018

@author: 陸
"""

from setting import follower,field,BattleDeck,makeCard,makeDeck,BattleSystem

def main():
    cardMaker = makeCard()
    Faiter = cardMaker.makeFollower(name="Faiter",cost=2,AP=2,HP=2)
    
    DeckMaker = makeDeck()
    print(DeckMaker.deck)
    Deck = DeckMaker.makeDeck(Faiter)
    BTDeck = BattleDeck(Deck)
    print(BTDeck.deck[0].name)
    print("Got Deck")
    
    BTSystem = BattleSystem()
    BTSystem.BattlePreparation(BTDeck,BTDeck)
    print(BTSystem.Field[0].playerName)
    BTSystem.turn(0)
    
    
    
    


if __name__ == '__main__':
    main()

