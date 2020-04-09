# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 23:08:00 2020

@author: Veronica
"""

import argparse
parser = argparse.ArgumentParser(description ='sort some integers.')

parser.add_argument('-lst')

parser.add_argument('integers', 
                    metavar ='N', 
                    type = float, 
                    nargs ='+', 
                    help ='an integer for the accumulator') 
  
parser.add_argument('sum', 
                    action ='store_const', 
                    const = sum) 
  
parser.add_argument('len', 
                    action ='store_const', 
                    const = len) 
  
args = parser.parse_args() 
add = args.sum(args.integers) 
length = args.len(args.integers) 
average = add / length 
print(average) 

