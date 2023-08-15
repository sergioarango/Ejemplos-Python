# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 09:55:07 2023

@author: Sergio
"""

#%%Ejercicio 1
#Escribir un programa que diga “Hola” a cualquiera que lo lea, preguntando la versión de Python que se está usando.
#Luego que permita ingresar una variable y luego imprima el tipo de variable que se ingresó.

#%%Desarrollo
print("Hola")

def obtener_tipo_variable(variable):
    try:
        variable = int(variable)
        return "int"
    except ValueError:
        try:
            variable = float(variable)
            return "float"
        except ValueError:
            return "str"

entrada_usuario = input("Ingresa una variable: ")
tipo = obtener_tipo_variable(entrada_usuario)
print("La variable ingresada es de tipo: " , tipo)