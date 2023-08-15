# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 10:57:28 2023

@author: Sergio
"""

#Ejercicio2
#Cree una función donde se retorne una lista de números consecutivos desde un límite inferior 
#designado por el usuario, hasta un número superior también ingresado por el usuario.


def lista (inf, sup):
    n=sup-inf
    numeros=[]
    for i in range (n):
        numeros.append(inf+i)
    numeros.append(sup)
    return numeros

inferior=int(input("ingrese el valor inferior: "))
superior=int(input("ingrese el valor superior: "))

Lista1=lista(inferior, superior)
        
        