# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 23:11:33 2018

@author: 陸
"""

from makecard import follower



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
        self.Extinction = []
        self.PlayerID = PlayerID
    
    def checkOutOfDeck(self):
        if len(self.BTDeck.deck) == 0:
            print("OutOfDeck")
            return True
        else: False  
        
    def GoToCementery(self,FieldID,Field):
        if FieldID <= 4:
            self.cemetery.append(self.place.pop(FieldID))
            self.cemetery[-1].lastWord(Field)
        elif FieldID <= 14:
            self.cemetery.append(self.hand.pop(FieldID-5))
    
    def checkDestroy(self,FieldID,Field):
        if self.place[FieldID].HP <= 0:
            self.GoToCementery(FieldID,Field)
        
    def draw(self,drawNum):
        for i in range(drawNum):
            if self.checkOutOfDeck():return True
            self.hand.append(self.BTDeck.deck.pop(0))
            if len(self.hand) >=10:
                self.cemetery.append(self.hand.pop(9))
        
    def PlayCard(self,handID,Field,PlayerID):
        self.place.append(self.hand.pop(handID))
        if len(self.place) >=6:
            self.Extinction.append(self.place.pop(5))
        else:
            self.place[-1].fanfare(Field,PlayerID)
    
    def PlaySpell(self,Spell,Field,PlayerID,handID):
        UseSpellFlag = Spell.PlaySpell(Field,PlayerID)
        if UseSpellFlag == True:
            self.cemetery.append(self.hand.pop(handID))
        
        
    def Marigan(self,):
        self.draw(3)
    
    def changeHP(self,plusHP):
        self.HP = self.HP + plusHP
        print(str(self.playerName) +"HP:" + str(self.HP))
    
    def info(self,):
        print("playerName:%s,HP:%d,MaxPP:%d,PP:%d,TurnNum:%d,len(hand):%d,len(place):%d,len(cemetery):%d" %(self.playerName,self.HP,self.MaxPP,self.PP,self.TurnNum,len(self.hand),len(self.place),len(self.cemetery)))
        print("Hand info")
        for card in self.hand:
            if card.cardType == "follower":
                print(card.name,card.AP,card.HP)
            elif card.cardType == "Amulet":
                print(card.name,card.count)
            elif card.cardType == "Spell":
                print(card.name)
        print("Place info")
        for card in self.place:
            if card.cardType == "follower":
                print(card.name,card.AP,card.HP,card.AttackFlag)
            elif card.cardType == "Amulet":
                print(card.name,card.count)
        
        

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
        Follower0.AttackFlag=1 #AttackFlagを攻撃済みに変更
        if self.Field[PlayerID].place[SelectFieldID].HP <= 0: #破壊判定処理
            self.Field[PlayerID].GoToCementery(SelectFieldID,self.Field)
        if self.Field[1-PlayerID].place[SelectEnemyFieldID].HP <= 0: #破壊判定処理
            self.Field[1-PlayerID].GoToCementery(SelectEnemyFieldID,self.Field)
            
    
    def AttackFace(self,Follower0,EnemyPlayer):
        EnemyPlayer.changeHP(-Follower0.AP)
        Follower0.AttackFlag=1 #AttackFlagを攻撃済みに変更
        
    def CostCheck(self,Field,cost):
        if  cost <= Field.PP:
            Field.PP -=cost
            return True
        else:
            print("コストが足りません error")
            return False
    def setPP(self,Field):
        Field.PP = Field.MaxPP
        
    def drawPhase(self,PlayerID):
        OutOfDeckFlag = self.Field[PlayerID].draw(1)
        return OutOfDeckFlag
    
    def StanbyFaze(self,PlayerID):
        for i in range(len(self.Field[PlayerID].place)):
            self.Field[PlayerID].place[i].StandbyPhase()
    
    def checkError(self,PlayerID):
        assert len(self.Field[PlayerID].hand)<=9
        assert len(self.Field[1-PlayerID].hand)<=9
        assert len(self.Field[PlayerID].place)<=5
        assert len(self.Field[1-PlayerID].place)<=5
        assert self.Field[PlayerID].MaxPP <= 10
        assert self.Field[1-PlayerID].MaxPP <= 10
    
    def turn(self,PlayerID):
        ENDFlag = 0
        self.Field[PlayerID].TurnNum += 1
        self.StanbyFaze(PlayerID)#フォロワーの攻撃を可能にする
        if self.Field[PlayerID].MaxPP<=9: self.Field[PlayerID].MaxPP += 1
        self.setPP(self.Field[PlayerID])
        OutOfDeckFlag = self.drawPhase(PlayerID)
        if OutOfDeckFlag == True: return 
        
        
        while ENDFlag == 0:
            print(str(self.Field[PlayerID].playerName) + "turn")
            SelectFieldID = int(input('カードを選択0~16>> ')) #0~4 placeのカード　5~13手札 14END 15自情報取得　16敵情報取得
            print(str(SelectFieldID))
            if SelectFieldID <= 4:#自分のPlace選択
                if SelectFieldID >= len(self.Field[PlayerID].place):print(str(SelectFieldID)+"Out of Place error")#自分のPlaceにカードがなかったらエラー
                else:
                    print(self.Field[PlayerID].place[SelectFieldID].name)
                    SelectCard = self.Field[PlayerID].place[SelectFieldID]
                    SelectEnemyFieldID = int(input('相手のカードか顔を選択0~5>> ')) #0~5 相手placeのカード　0~4手札 5顔
                    print(str(SelectEnemyFieldID))
                    if SelectEnemyFieldID <=5 and  self.Field[PlayerID].place[SelectFieldID].AttackFlag == 1:
                        print(str(self.Field[PlayerID].place[SelectFieldID]) + "は攻撃できません error")#召喚酔い・攻撃済みだったらエラー
                    elif SelectEnemyFieldID <=4:#相手のPlace選択
                        if SelectEnemyFieldID >= len(self.Field[1-PlayerID].place):print("Out of Place error")#相手のPlaceにカードがなかったらエラー
                        else:
                            Enemy = self.Field[1-PlayerID].place[SelectEnemyFieldID]
                            print("Enemy")
                            print(Enemy.name)
                            self.fight(SelectCard,Enemy,SelectFieldID,SelectEnemyFieldID,PlayerID)#交戦
                    
                    elif SelectEnemyFieldID == 5:#相手の顔選択
                        EnemyPlayer = self.Field[1-PlayerID]
                        self.AttackFace(SelectCard,EnemyPlayer)
                    
                    else: print("0~5を入力してください") #入力値がエラー
                
                
            elif SelectFieldID <=13:#自分の手札選択
                SelectHandID = SelectFieldID - 5 
                if SelectHandID >= len(self.Field[PlayerID].hand):print("Out of Hand error")#自分のHandにカードがなかったらエラー
                elif self.CostCheck(self.Field[PlayerID],self.Field[PlayerID].hand[SelectHandID].cost) == False:print("PPがたりません error")
                elif self.Field[PlayerID].hand[SelectHandID].cardType == "Spell": #スペルを選択した時
                    self.Field[PlayerID].PlaySpell(self.Field[PlayerID].hand[SelectHandID],self.Field,PlayerID,SelectHandID)
                elif len(self.Field[PlayerID].place) >= 5:print("Place が埋まっています error")
                else:
                    print(self.Field[PlayerID].hand[SelectHandID].name)
                    self.Field[PlayerID].PlayCard(SelectHandID,self.Field,PlayerID)
            
            elif SelectFieldID <= 14:#END
                print(str(self.Field[PlayerID].playerName) + "END")
                ENDFlag = 1
            elif SelectFieldID == 15:#自分の情報
                self.Field[PlayerID].info()
            elif SelectFieldID == 16:#相手の情報
                self.Field[1-PlayerID].info()
            else:
                print("Unexpected Number.You should select from 0 to 16. error")
             
            self.checkError(PlayerID)
            print("PlayerHP")
            print(self.Field[PlayerID].HP,self.Field[1-PlayerID].HP)
            if self.Field[PlayerID].HP <= 0 or self.Field[1-PlayerID].HP<=0:
                return 
                
                
        self.turn(1-PlayerID)
        

        
        

    
        

        
            
        
        