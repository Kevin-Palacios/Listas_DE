"""
Palacios Elizondo Kevin Antonio
2BM1
Inteligencia Artificial
24/04/2022 
q:)->-</: 
"""
#from sympy import true
import time

from funciones_Listas_DE import *

import sys
sys.path.insert(1, 'Listas_DE')
from clases import lista
from clases import Nodo
from clases import Dato

c = crearLista()


#entrada = int(input("Ingrese cuantos numeros va a ingresar: "))
opcion=0

while(opcion!=10):
    print("Que quieres hacer?")
    print("1-Ingresar nodo por la derecha")
    print("2-Ingresar nodo por la izquierda")
    print("3-Ingresar nodo por la posición n")
    print("4-Eliminar ultimo nodo")
    print("5-Eliminar primer nodo")
    print("6-Eliminar nodo en la posición n")
    print("7-Mostrar todos los nodos")
    print("8-Contar Nodos")
    print("9-Borrar lista")
    print("10-Salir")
    opcion=int(input())
    if(opcion==1):
        datoIngreso=str(input("Ingresa el dato: "))
        agregarDerecha(c, datoIngreso)
        print("Nodo ingresado por la derecha")
    elif(opcion==2):
        datoIngreso=str(input("Ingresa la ruta del archivo: "))
        c=agregarIzq(c, datoIngreso)
    elif(opcion==3):
        n=int(input("Ingresa la posición donde quieras agregar el nodo: "))
        datoIngreso=str(input("Ingresa el dato: "))
        c=agregarN(c, datoIngreso, n)
    elif(opcion==4):
        datoExtraido = extraerD(c)
        print("Dato extraido por la derecha: "+str(datoExtraido))
    elif(opcion==5):
        extraerI(c)
    elif(opcion==6):
        n= int(input("Ingresa la posición que quieras eliminar: "))
        datoExtraido= extraerN(c, n)
        print("Dato extraido por la pos "+str(n)+": "+str(datoExtraido))
    elif(opcion==7):
        c = recorrerLista(c)
    elif(opcion==8):
        num_nodos=contarNodos(c)
        print(num_nodos)
    elif(opcion==9):
        borrarLista(c)
    elif(opcion==10):
        print("Adios")
    else:
        print("opcion no válida, ingresa una válida")