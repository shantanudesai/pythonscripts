#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 20:50:42 2018

@author: shantanu
"""

def diff(lista,listb):
    listc = []
    for i in lista:
        if i in listb:
            listc.append(i)
    
    uniqueList = []
    for elem in listc:
        if elem not in uniqueList:
            uniqueList.append(elem)       
      
    return uniqueList


lista = open('a.txt').read().split()
listb = open('b.txt').read().split()

print(diff(lista,listb),len(diff(lista,listb)))

