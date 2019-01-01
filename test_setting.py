#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 00:00:06 2018

@author: riku
"""
import unittest
from main import main
from io import StringIO
import contextlib
from parameterized import parameterized, param
import numpy as np

class redirect_stdin(contextlib._RedirectStream):
    _stream = "stdin"
    
inputDatas = []
class Test(unittest.TestCase):
    
    def makeInputDataHP(self,commnet):
        data = "14\n14\n14\n14\n"
        for i in range(200):
            data += "6\n15\n16\n14\n6\n15\n16\n14\n0\n5\n14\n6\n15\n16\n0\n5\n1\n5\n14\n"
        return data
    
    def makeInputDataDeck(self,commnet):
        data = "14\n14\n14\n14\n"
        for i in range(200):
            data += "14\n15\n16\n14\n15\n16\n14\n15\n16\n14\n15\n16\n"
        return data
    
    def makeInputDataRandom(self,commnet):
        data = ""
        for i in range(20000):
            command = np.random.randint(0,17)
            data += str(command) + "\n"
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
        for i in range(10):
            inputDatas.append(self.makeInputDataRandom(""))
#        print(inputDatas)
        print("setup")
    
#    @parameterized.expand([param(DataID=0),param(DataID=1)])
    @parameterized.expand([param(DataID=0),param(DataID=1),param(DataID=2),param(DataID=3),param(DataID=4),param(DataID=5),param(DataID=6),param(DataID=7),param(DataID=8),param(DataID=9)])
    def test_turn(self,DataID):
        data = inputDatas[DataID]
        buf = self.setFile(data)
        with redirect_stdin(buf):
            result =  main()
        assert result == True
        
        

        
    def teardown_method(self):
        BattleSystem.BSinput = input

if __name__ == "__main__":
    unittest.main()



