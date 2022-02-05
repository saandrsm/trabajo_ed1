# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 18:59:41 2022

@author: solet
"""

print("Calculadora")
print("---------------------------------------------")
print("Selección de operación")
print("\t1.-Suma de dos números")
print("\t2.-Resta")
print("\t3.-Multiplicación")
print("\t4.-División")
print("\t5.-Cociente")
print("\t6.-Resto de división")
print("\t7.-Exponenciación")
print("\t8.-Area de un círculo")
print("\t9.-Area de un triángulo")
print("---------------------------------------------")
opc = int(input("Introduzca una opción: "))

if(opc==1):
    x=int(input("Introduzca el primer número:  "))
    y=int(input("Introduzca el segundo número: "))
    print(f"{x}+{y}={x+y}")
elif(opc==2):
    x=int(input("Introduzca el primer número:  "))
    y=int(input("Introduzca el segundo número: "))
    print(f"{x}-{y}={x-y}")
elif(opc==3):
    x=int(input("Introduzca el primer número:  "))
    y=int(input("Introduzca el segundo número:  "))
    print(f"{x}*{y}={x*y}")