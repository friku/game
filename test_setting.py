#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 00:00:06 2018

@author: riku
"""
import sys
import pytest
import unittest
from main import main
from setting import follower,field,BattleDeck,makeCard,makeDeck,BattleSystem
from io import StringIO
import contextlib
from parameterized import parameterized, param

class redirect_stdin(contextlib._RedirectStream):
    _stream = "stdin"
    
inputDatas = []
class Test(unittest.TestCase):
    
    def makeInputDataHP(self,commnet):
        data = "14\n14\n14\n14\n"
        for i in range(20):
            data += "6\n15\n16\n14\n6\n15\n16\n14\n0\n5\n14\n6\n15\n16\n0\n5\n1\n5\n14\n"
        return data
    
    def makeInputDataDeck(self,commnet):
        data = "14\n14\n14\n14\n"
        for i in range(20):
            data += "14\n14\n14\n14\n"
        return data
    
    def setFile(self,data):
        buf = StringIO()
        buf.write(data)
        buf.seek(0)
        return buf
    
    def setUp(self):
        global inputDatas
        inputDatas.append(self.makeInputDataHP(""))
        inputDatas.append(self.makeInputDataDeck(""))
        print(inputDatas)
        print("setup")
    
    @parameterized.expand([param(DataID=0),param(DataID=1)])
    def test_turn(self,DataID):
        data = inputDatas[DataID]
        print("inputData")
        print(data)
        buf = self.setFile(data)
        print(buf)
        with redirect_stdin(buf):
            result =  main()
        assert result == True
        
        

        
    def teardown_method(self):
        BattleSystem.BSinput = input

if __name__ == "__main__":
    unittest.main()



