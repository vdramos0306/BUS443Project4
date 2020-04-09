# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 23:09:12 2020

@author: Vernonica
"""

import sys 
output = ""
for word in sys.argv[2:]:
    result = ""
    for x in word:
        if x not in result:
            result += x
        output +=(result+"")
    output = output[:-1]
    print(output)
