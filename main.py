# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 23:55:18 2018

@author: 陸
"""

from setting import follower,field,BattleDeck,makeCard,makeDeck

def main():
    cardMaker = makeCard()
    Faiter = cardMaker.makeFollower(name="Faiter",cost=2,AP=2,HP=2)
    
    DeckMaker = makeDeck()
    print(DeckMaker.deck)
    Deck = DeckMaker.makeDeck(Faiter)
    BTDeck = BattleDeck(Deck)
    print(BTDeck.deck[0].name)
    print("Got Deck")
    
    Field1 = field("player1",BTDeck)
    print(Field1.BTDeck.deck[0].name)
    
    #Marigan
    Field1.Marigan()
    print(Field1.hand[0].name)
    
    Field1.PlayCard(0)
    print("place")
    print(Field1.place[0].name)
    
    
    
    


if __name__ == '__main__':
    main()

