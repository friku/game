#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 15:20:38 2018

@author: riku
"""

def selectMyPlace(Field,PlayerID,fanfareFlag=0):
    selectFlag = 0
    while selectFlag == 0:
        SelectFieldID = int(input('カードを選択0~4>> ')) #0~4 placeのカード　5~13手札 14END 15自情報取得　16敵情報取得
        if SelectFieldID >= (len(Field[PlayerID].place)-fanfareFlag):#選択したplaceにカードがない
            print("error")
            selectFlag = 0
        else:
            return SelectFieldID