#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 02:45:08 2018

@author: riku
"""
from Utils import selectMyPlace,selectEnemyPlace,evolveChangeStatus,addRush,ReduceDamage

class card:
    def __init__(self,name,cost,Enhance=[100],Accelerate=None):
        self.name = name
        self.cost = cost
        self.Enhance = Enhance
        self.Accelerate = Accelerate
        self.EnhanceNumber = -1 #0以上ならEnhanceを実行する。
    
    def fanfare(self,Field,PlayerID):
        print("fanfare pass")
        pass
    
    def lastWord(self,Field):
        print("fanfare pass")
        pass
    
    def EndPhase(self,Field,PlayerID):
        pass
    

class follower(card):
    def __init__(self,name,cost,AP,HP,EAP=2,EHP=2,Enhance=[100],Accelerate=None):
        card.__init__(self,name,cost,Enhance=Enhance,Accelerate=Accelerate)
        self.AP = AP
        self.HP = HP
        self.EAP = EAP
        self.EHP = EHP
        self.MaxAP = AP
        self.MaxHP = HP
        self.SummonFlag = 1
        self.AttackFlag = 0
        self.EvolveFlag = 0
        self.RushFlag = 0
        self.StormFlag = 0
        self.BaneFlag = 0
        self.WardFlag = 0
        self.ReduceDamage = 0
        self.cardType = "follower"
        
    def changeHP(self,plusHP,Field,PlayerID):
        if self.ReduceDamage == -1:
            plusHP = 0
        elif self.ReduceDamage <= plusHP:
            plusHP -= self.ReduceDamage
        else:
            plusHP = 0
        self.HP = self.HP + plusHP
        print(str(self.name) +"HP:" + str(self.HP))
        return self.HP
    
    def StandbyPhase(self,):
        self.SummonFlag = 0
        self.AttackFlag = 0
    
    def evolution(self,Field,PlayerID):
        evolveChangeStatus(self)
        
class Amulet(card):
    def __init__(self,name,cost,count=None):
        card.__init__(self,name,cost)
        self.count = count
        self.cardType = "Amulet"
    
    def changeCount(self,plusCount):
        self.count = self.count + plusCount
        print(str(self.name) +"count:" + str(self.count))
        return self.count
    
    def StandbyPhase(self,):#オーバーライドして使う
        pass    

class Spell(card):
    def __init__(self,name,cost,Enhance=[100],Accelerate=None):
        card.__init__(self,name,cost,Enhance=Enhance,Accelerate=Accelerate)
        self.cardType = "Spell"
    
    def PlaySpell(self,Field,PlayerID):#オーバーライドして使う
        return True

class BubetuNoSinja(follower):
    def __init__(self,name="BubetuNoSinja",cost=1,AP=1,HP=1,):
        follower.__init__(self,name,cost,AP,HP)
        self.AP = AP
        self.HP = HP
        self.AttackFlag = 1
        self.cardType = "follower"
        
    def fanfare(self,Field,PlayerID):
        print("fanfare:"+str(self.name))
        if len(Field[PlayerID].place)>=2:
            SelectFieldID = selectMyPlace(Field,PlayerID,fanfareFlag=1)
            Field[PlayerID].place[SelectFieldID].changeHP(-1,Field,PlayerID)
            Field[PlayerID].checkDestroy(SelectFieldID,Field)
            Field[PlayerID].draw(1)

class BubetuNoEnsou(Spell):
    def __init__(self,name="BubetuNoEnsou",cost=1):
        super().__init__(name,cost)
        self.cardType = "Spell"
        
    def PlaySpell(self,Field,PlayerID):
        if len(Field[PlayerID].place) == 0: return False
        if len(Field[1-PlayerID].place) == 0: return False
        
        SelectFieldID = selectMyPlace(Field,PlayerID,fanfareFlag=0)
        SelectEnemyFieldID = selectEnemyPlace(Field,PlayerID)
        Field[PlayerID].place[SelectFieldID].changeHP(-1,Field,PlayerID)
        Field[PlayerID].checkDestroy(SelectFieldID,Field)
        Field[1-PlayerID].place[SelectEnemyFieldID].changeHP(-3,Field,PlayerID)
        Field[1-PlayerID].checkDestroy(SelectEnemyFieldID,Field)
        return True
        
class Aira(follower):
    def __init__(self,name="Aira",cost=2,AP=2,HP=2,):
        follower.__init__(self,name,cost,AP,HP)
        self.AP = AP
        self.HP = HP
        self.AttackFlag = 1
        self.cardType = "follower"
        
    def evolution(self,Field,PlayerID):
        evolveChangeStatus(self)
        if Field[PlayerID].MaxPP <= 9:
            Field[PlayerID].MaxPP +=1

class WhitefrostWhisper(Spell):
    def __init__(self,name="WhitefrostWhisper",cost=2):
        super().__init__(name,cost)
        self.cardType = "Spell"
        
    def PlaySpell(self,Field,PlayerID):
        if len(Field[1-PlayerID].place) == 0: return False
        
        SelectEnemyFieldID = selectEnemyPlace(Field,PlayerID)
        if Field[1-PlayerID].place[SelectEnemyFieldID].HP < Field[1-PlayerID].place[SelectEnemyFieldID].MaxHP:
            Field[1-PlayerID].GoToCementery(SelectEnemyFieldID,Field)
        else:
            Field[1-PlayerID].place[SelectEnemyFieldID].changeHP(-1,Field,PlayerID)
            Field[1-PlayerID].checkDestroy(SelectEnemyFieldID,Field)
        return True
 
class Filene(follower):
    def __init__(self,name="Filene",cost=2,AP=1,HP=3):
        follower.__init__(self,name,cost,AP,HP)
        self.AP = AP
        self.HP = HP
        self.EAP = 1
        self.EHP = 1
        self.AttackFlag = 1
        self.cardType = "follower"
        
    def fanfare(self,Field,PlayerID):
        print("fanfare:"+str(self.name))
        if len(Field[PlayerID].hand) <=8:
            Field[PlayerID].hand.append(WhitefrostWhisper())
     

    def evolution(self,Field,PlayerID):
        evolveChangeStatus(self)
        if len(Field[1-PlayerID].place) == 0: return False
        SelectEnemyFieldID = selectEnemyPlace(Field,PlayerID)
        Field[1-PlayerID].place[SelectEnemyFieldID].changeHP(-1,Field,PlayerID)
        Field[1-PlayerID].checkDestroy(SelectEnemyFieldID,Field)
        return True
    
class ServantOfDisdain(follower):
    def __init__(self,name="ServantOfDisdain",cost=2,AP=2,HP=2):
        follower.__init__(self,name,cost,AP,HP)
        self.AP = AP
        self.HP = HP
        self.AttackFlag = 1
        self.cardType = "follower"
    
    def changeHP(self,plusHP,Field,PlayerID):
        if self.ReduceDamage == -1:
            plusHP = 0
        elif self.ReduceDamage <= plusHP:
            plusHP -= self.ReduceDamage
        else:
            plusHP = 0
        self.HP = self.HP + plusHP
        print(str(self.name) +"_HP:" + str(self.HP))
        print(self.HP,plusHP)
        if self.HP >=1 and plusHP <=0:
            Field[PlayerID].draw(1)
        return self.HP

class DragonOracle(Spell):
    def __init__(self,name="DragonOracle",cost=2):
        super().__init__(name,cost)
        self.cardType = "Spell"
        
    def PlaySpell(self,Field,PlayerID):
        if Field[PlayerID].MaxPP >= 7:
            Field[PlayerID].draw(1)
        if Field[PlayerID].MaxPP <= 9:
            Field[PlayerID].MaxPP +=1
        return True

class VileVioletDragon(follower):
    def __init__(self,name="VileVioletDragon",cost=5,AP=4,HP=4):
        follower.__init__(self,name,cost,AP,HP)
        self.AP = AP
        self.HP = HP
        self.AttackFlag = 1
        self.cardType = "follower"
    
    def changeHP(self,plusHP,Field,PlayerID):
        if self.ReduceDamage == -1:
            plusHP = 0
        elif self.ReduceDamage <= plusHP:
            plusHP -= self.ReduceDamage
        else:
            plusHP = 0
        self.HP = self.HP + plusHP
        print(str(self.name) +"_HP:" + str(self.HP))
        print(self.HP,plusHP)
        if self.HP >=1 and plusHP <=0:
            Field[PlayerID].draw(2)
        return self.HP   

class Megalorca(follower):
    def __init__(self,name="Megalorca",cost=2,AP=2,HP=2):
        follower.__init__(self,name,cost,AP,HP)
        self.AP = AP
        self.HP = HP
        self.AttackFlag = 1
        self.cardType = "follower"
    

class WatersOfTheOrca(Spell):
    def __init__(self,name="WatersOfTheOrca",cost=2,Enhance=[4,6,8,10]):
        super().__init__(name,cost,Enhance=Enhance)
        self.cardType = "Spell"
        
    def PlaySpell(self,Field,PlayerID):
        if self.EnhanceNumber == -1:
            Field[PlayerID].place.append(Megalorca())
        elif self.EnhanceNumber == 0:
            for i in range(2):
                Field[PlayerID].place.append(Megalorca())
        elif self.EnhanceNumber == 1:
            for i in range(3):
                Field[PlayerID].place.append(Megalorca())
        elif self.EnhanceNumber == 2:
            for i in range(4):
                Field[PlayerID].place.append(Megalorca())
        elif self.EnhanceNumber == 3:
            for i in range(5):
                Field[PlayerID].place.append(Megalorca())
        
        for i in range(5):
            if len(Field[PlayerID].place) >=6:
                Field[PlayerID].Extinction.append(Field[PlayerID].place.pop(5))#placeからあふれたカードを消滅
        return True

class MasamuneRagingDragon(follower):
    def __init__(self,name="MasamuneRagingDragon",cost=2,AP=2,HP=2):
        super().__init__(self,name,cost,AP,HP)
        self.cardType = "follower"
        self.BaneFlag = 1 
        
        
    def fanfare(self,Field,PlayerID):
        print("fanfare:"+str(self.name))
        if Field[PlayerID].MaxPP < 10:
            pass
        else:
            for i in range(len(Field[PlayerID])):
                addRush(Field,PlayerID,i)#突進付与
                ReduceDamage(Field,PlayerID,i,-1)#ダメージ軽減
        return True

        
        #戦闘準備用
class BattleDeck:
    deck = []
    def __init__(self,deck):
        self.deck = deck
        
    def addCardToDeck(self,card):
        self.deck.append(card)
  
  
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