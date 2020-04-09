# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 23:09:50 2020

@author: Veronica
"""

import sys
result = []
temp = None
for word in sys.argv[1:]:
    if word=="-lst":
        if temp!=None:
            result.append(temp)
        temp = []
    else:
        temp.append(int(word)**2)
result.append(temp)
print(result)
