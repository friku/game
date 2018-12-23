#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 17:31:40 2018

@author: riku
"""

import pytest
import unittest
from main import main
from setting import follower,field,BattleDeck,makeCard,makeDeck,BattleSystem

class TestMain(unittest.TestCase):
        
    def test_main(self):
        main()
        pass

if __name__ == "__main__":
    unittest.main()