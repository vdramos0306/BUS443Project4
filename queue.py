# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 23:10:54 2020

@author: Vernonica
"""

class Queue:
    def __init__(self):
        self.queuecar = []
    
    def isEmpy(self):
        return self.queuecar ==[]
    
    def addToQueue(self, car):
        self.queuecar.append(car)
    
    def popFromQueue(self):
        return self.queuecar.pop(0)
    
    def sizeOfQueue(self):
        return len(self.queuecar)
    
newitem = Queue()
newitem.addToQueue('car1')
newitem.sizeOfQueue()
newitem.sizeOfQueue()
newitem.popFromQueue()