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

class redirect_stdin(contextlib._RedirectStream):
    _stream = "stdin"

class Test(unittest.TestCase):
    def makeInputData(self,commnet):
        data = ""
        for i in range(6):
            data += "14\n14\n14\n14\n6\n15\n16\n14\n6\n15\n16\n14\n6\n15\n16\n14\n0\n0\n14\n6\n15\n16\n14\n6\n15\n16\n14\n6\n15\n16\n14\n0\n5\n"
        return data
    
    def test_turn(self):
        inputDatas = self.makeInputData("null")
        buf = StringIO()
        buf.write(inputDatas)
        buf.seek(0)
        with redirect_stdin(buf):
            result =  main()
        assert result == True
        
        
    def setUp(self):
        pass
        
    def teardown_method(self):
        BattleSystem.BSinput = input

if __name__ == "__main__":
    unittest.main()



