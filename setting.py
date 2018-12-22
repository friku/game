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
        
    def changeHP(self,plusHP):
        self.HP = self.HP + plusHP
        print(self.HP)
        

        

class field:
    HP = 20
    PP = 0
    
    TurnNum = 0
    
    def __init__(self,playerName,BTDeck,PlayerID):
        self.playerName = playerName
        self.BTDeck = BTDeck
        self.hand = []
        self.place = []
        self.PlayerID = PlayerID
        
    def draw(self,drawNum):
        for i in range(drawNum):
            self.hand.append(self.BTDeck.deck.pop(0))
        
    def PlayCard(self,handID):
        card = self.hand[handID]
        self.place.append(card)
        
    def Marigan(self,):
        self.draw(3)
    
    def changeHP(self,plusHP):
        self.HP = self.HP + plusHP
        print(str(self.playerName) +"HP:" + str(self.HP))
 

class BattleSystem:
    def BattlePreparation(self,BTDeck0,BTDeck1):
        self.Field = []
        self.Field.append(field("player0",BTDeck0,0))
        self.Field.append(field("player1",BTDeck1,1))
        self.Field[0].Marigan()
        self.Field[1].Marigan()
    
    def changeTurn(self,PlayerID,turn):
        NextPlayerID = 1-PlayerID
        turn(NextPlayerID)
    
    def fight(self,Follower0,Follower1):
        Follower0.changeHP(-Follower1.AP)
        Follower1.changeHP(-Follower0.AP)
    
    def AttackFace(self,Follower0,EnemyPlayer):
        EnemyPlayer.changeHP(-Follower0.AP)
    
    
        
        
    
    def turn(self,PlayerID):
        ENDFlag = 0
        while ENDFlag == 0:
            print(str(self.Field[PlayerID].playerName) + "turn")
            SelectCard = int(input('カードを選択0~14>> ')) #0~4 placeのカード　5~13手札 14END
            
            if SelectCard <= 4:
                print(self.Field[PlayerID].place[SelectCard].name)
                SelectCard = self.Field[PlayerID].place[SelectCard]
                SelectEnemyCardID = int(input('相手のカードか顔を選択0~5>> ')) #0~5 相手placeのカード　0~4手札 5顔
                if SelectEnemyCardID <=4:
                    Enemy = self.Field[1-PlayerID].place[SelectEnemyCardID]
                    print("Enemy")
                    print(Enemy)
                    self.fight(SelectCard,Enemy)
                elif SelectEnemyCardID == 5:
                    EnemyPlayer = self.Field[1-PlayerID]
                    self.AttackFace(SelectCard,EnemyPlayer)
               
                
                
            elif SelectCard <=13:
                SelectHandID = SelectCard - 5 
                print(self.Field[PlayerID].hand[SelectHandID].name)
                self.Field[PlayerID].PlayCard(SelectHandID)
            
            elif SelectCard == 14:
                print(str(self.Field[PlayerID].playerName) + "END")
                ENDFlag = 1
            else:
                print("Unexpected Number.You should select from 0 to 14.")
        self.turn(1-PlayerID)
        
        
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
        
            
        
        