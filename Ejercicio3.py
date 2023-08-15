# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 12:00:54 2023

@author: Sergio
"""

#Ejercicio 3
#Cree una función donde el usuario pueda realizar operaciones matemáticas básicas entre dos números



def bascicalculator (a,b,operacion):
    if operacion == "Suma":
        c=a+b
    elif operacion == "Resta":
        c=a-b
    elif operacion == "Multiplicacion":
        c=a*b
    return c

Number1=float(input("numero 1: "))
Number2=float(input("numero 2: "))
operacion=input("ingrese la opercion: ")

resultado=bascicalculator(Number1, Number2, operacion)

print("El resultado de la operación es: ", resultado)
    