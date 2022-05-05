# -*- coding: utf-8 -*-
"""
Created on Thu May  5 11:14:35 2022

@author: sabsriha
"""

# stack program

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
        #return not self.items
    
    def push(self,item):
        self.items.append(item)