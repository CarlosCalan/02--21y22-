# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 23:24:44 2020

@author: Carlos1
"""
def findInternet(mensaje):
    palabra='Internet'in mensaje
    return (palabra)

print(findInternet('El mensaje tiene nternet'))