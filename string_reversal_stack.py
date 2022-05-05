# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:57:50 2022

@author: sabsriha
"""

import stack_program

string = "Learn a lot with LinkedIn Learning"
reversed_string=""
s = stack_program.Stack()

for char in string:
    s.push(char)

while not s.is_empty():
    reversed_string += s.peek()
    s.pop()

print(reversed_string)