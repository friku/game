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
        print(str(self.name) +"HP:" + str(self.HP))
        return self.HP
        

class field:
    def __init__(self,playerName,BTDeck,PlayerID):
        self.HP = 20
        self.PP = 0
        self.MaxPP = 0
        self.TurnNum = 0
        self.cemetery = []
        self.playerName = playerName
        self.BTDeck = BTDeck
        self.hand = []
        self.place = []
        self.PlayerID = PlayerID
        
        
    def draw(self,drawNum):
        for i in range(drawNum):
            self.hand.append(self.BTDeck.deck.pop(0))
        
    def PlayCard(self,handID):
        self.place.append(self.hand.pop(handID))
        
    def Marigan(self,):
        self.draw(3)
    
    def changeHP(self,plusHP):
        self.HP = self.HP + plusHP
        print(str(self.playerName) +"HP:" + str(self.HP))
    
    def GoToCementery(self,FieldID):
        if FieldID <= 4:
            self.cemetery.append(self.place.pop(FieldID))
        elif FieldID <= 14:
            self.cemetery.append(self.hand.pop(FieldID-5))
    
    def info(self,):
        print("playerName,HP,PP,TurnNum,len(hand),len(place)")
        print(self.playerName,self.HP,self.MaxPP,self.PP,self.TurnNum,len(self.hand),len(self.place),len(self.cemetery))
        print("Hand info")
        for card in self.hand:
            print(card.name,card.HP,card.AP)
        print("Place info")
        for card in self.place:
            print(card.name,card.HP,card.AP)
        
        

class BattleSystem:
    def BattlePreparation(self,BTDeck0,BTDeck1):
        self.Field = []
        self.Field.append(field("player0",BTDeck0,0))
        self.Field.append(field("player1",BTDeck1,1))
        self.Field[0].Marigan()
        self.Field[1].Marigan()
    
    
    def fight(self,Follower0,Follower1,SelectFieldID,SelectEnemyFieldID,PlayerID):#交戦処理
        Follower0.changeHP(-Follower1.AP)
        Follower1.changeHP(-Follower0.AP)
        if self.Field[PlayerID].place[SelectFieldID].HP <= 0: #破壊判定処理
            self.Field[PlayerID].GoToCementery(SelectFieldID)
        if self.Field[1-PlayerID].place[SelectEnemyFieldID].HP <= 0: #破壊判定処理
            self.Field[1-PlayerID].GoToCementery(SelectEnemyFieldID)
    
#    def PostFight(self,)#交戦後処理
        
    
    def AttackFace(self,Follower0,EnemyPlayer):
        EnemyPlayer.changeHP(-Follower0.AP)
        
    def CostCheck(self,Field,cost):
        if  cost <= Field.PP:
            Field.PP -=cost
            return True
        else:
            print("コストが足りません")
            return False
    def setPP(self,Field):
        Field.PP = Field.MaxPP
    
    
    def turn(self,PlayerID):
        ENDFlag = 0
        self.Field[PlayerID].MaxPP += 1
        self.setPP(self.Field[PlayerID])
        while ENDFlag == 0:
            print(str(self.Field[PlayerID].playerName) + "turn")
            SelectFieldID = int(input('カードを選択0~15>> ')) #0~4 placeのカード　5~13手札 14END 15自情報取得　16敵情報取得
            
            if SelectFieldID <= 4:#自分のPlace選択
                print(self.Field[PlayerID].place[SelectFieldID].name)
                SelectCard = self.Field[PlayerID].place[SelectFieldID]
                SelectEnemyFieldID = int(input('相手のカードか顔を選択0~5>> ')) #0~5 相手placeのカード　0~4手札 5顔
                
                if SelectEnemyFieldID <=4:#相手のPlace選択
                    Enemy = self.Field[1-PlayerID].place[SelectEnemyFieldID]
                    print("Enemy")
                    print(Enemy)
                    self.fight(SelectCard,Enemy,SelectFieldID,SelectEnemyFieldID,PlayerID)#交戦
                    
                elif SelectEnemyFieldID == 5:#相手の顔選択
                    EnemyPlayer = self.Field[1-PlayerID]
                    self.AttackFace(SelectCard,EnemyPlayer)
                
                
            elif SelectFieldID <=13:#自分の手札選択
                SelectHandID = SelectFieldID - 5 
                print(self.Field[PlayerID].hand[SelectHandID].name)
                SelectCardCost = self.Field[PlayerID].hand[SelectHandID].cost
                if self.CostCheck(self.Field[PlayerID],SelectCardCost) == True:
                    self.Field[PlayerID].PlayCard(SelectHandID)
            
            elif SelectFieldID <= 14:#END
                print(str(self.Field[PlayerID].playerName) + "END")
                ENDFlag = 1
            elif SelectFieldID == 15:#自分の情報
                self.Field[PlayerID].info()
            elif SelectFieldID == 16:#相手の情報
                self.Field[1-PlayerID].info()
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
    def makeDeck(self,cards):
        deck = []
        for i in range(40):
            deck.append(card)
        return deck
        
            
        
        