# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 18:57:38 2023

@author: 84908
"""
import random

print("Test Eval")
equation = 'x1 + 2 * x2 + x3'

def modify_value(x1,x2,x3):
    result = eval(equation)
    print(result)
    return result

#a = 5
#modify_value(a, 2, 3)
x1 = random.randint(3, 9)
x2 = random.randint(10, 19)
x3 = random.randint(20, 29)
modify_value(x1, x2, x3)