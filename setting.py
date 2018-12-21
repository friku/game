# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 23:11:33 2018

@author: 陸
"""

class card:
    def __init__(self,name,cost):
        self.name = name
        self.cost = cost

class follower(card):
    def __init__(self,name,cost,AP,HP):
        card.__init__(self,name,cost)
        self.AP = AP
        self.HP = HP
        
    def attack(self,enemy):
        self.HP = self.HP - enemy.AP
        enemy.atacked(self)
        
    def attacked(self,enemy):
        self.HP = self.HP - enemy.AP
        

class field:
    HP = 20
    PP = 0
    
    def __init__(self,playerName,BTDeck):
        self.playerName = playerName
        self.BTDeck = BTDeck
        self.hand = []
        self.place = []
        
    def draw(self,drawNum):
        for i in range(drawNum):
            self.hand.append(self.BTDeck.deck.pop(0))
        
    def PlayCard(self,handID):
        card = self.hand[handID]
        self.place.append(card)
        
    def Marigan(self,):
        self.draw(3)
 

class BattleSystem:
    def BattlePreparation(self,BTDeck1,BTDeck2):
        Field1 = field("player1",BTDeck1)
        Field2 = field("player2",BTDeck2)
        Field1.Marigan()
        Field2.Marigan()
        
class BattleDeck:
    deck = []
    def __init__(self,deck):
        self.deck = deck
        
    def addCardToDeck(self,card):
        self.deck.append(card)
    
    
        
#戦闘準備用
class makeCard:
    def makeFollower(self,name,cost,AP,HP):
        card = follower(name,cost,AP,HP)
        return card
        
class makeDeck:
    deck = []
        
    def makeDeck(self,card):
        for i in range(40):
            self.deck.append(card)
        return self.deck
        
            
        
        