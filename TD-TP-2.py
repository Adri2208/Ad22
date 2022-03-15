#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:00:47 2022

@author: adri22
"""


#exercice 1

lg=int(input("donnez un nombre entre 1 et 500 : "))
seuil=int(input("donnez un nombre entre 1 et 500 : "))

if lg<seuil :
    print("invalide")
    
else: 
    print("valide")
    
#exercice 2

for i in range (0,16):
    range(i)
    print(i)
    

#exercice 3


liste=[]
i=int(input("nombre:"))

while i != -1 :
    liste.append(i)
    i=int(input("autre nombre:"))
    
print(liste)