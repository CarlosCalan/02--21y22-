# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 23:02:39 2020

@author: Carlos1
"""
def GetDomain(dominio):
    x=0
    for val in dominio:
        if val=="@":
            x=1
        if x==1:    
            print(val, end='')
            
GetDomain('user@domain.com')
        