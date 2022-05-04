"""
Palacios Elizondo Kevin Antonio
2BM1
Inteligencia Artificial
24/04/2022 
q:)->-</: 
"""
import sys
from tkinter.messagebox import NO

sys.path.insert(1, 'Listas_DE')
from clases import lista
from clases import Nodo
from clases import Dato


def crearLista():
    l=lista(0)
    l.cabecera=None
    return l

def agregarDerecha(l, datoIngreso):
    nodousuario=Nodo()
    nodousuario.dato=datoIngreso
    if(estaVacia(l)):
        l.cabecera=nodousuario
        l.cabecera.siguiente=None
        l.cabecera.anterior=None
        l.cabecera.pos=0
    else:
        nodoAux= Nodo()
        nodoAux = l.cabecera
        while(nodoAux.siguiente!=None):
            nodoAux=nodoAux.siguiente
        
        posAux = nodoAux.pos
        nodousuario.siguiente=None
        nodousuario.anterior=nodoAux
        nodousuario.pos=posAux+1
        nodoAux.siguiente=nodousuario
    l.cursor=l.cursor+1

def agregarIzq(l, datoIngreso):
    listaAux = crearLista()

    nodousuario=Nodo()
    
    if(estaVacia(l)):
        agregarDerecha(l, datoIngreso)
        return l
    else:
        nodousuario.dato=datoIngreso
        agregarDerecha(listaAux, datoIngreso)
        while(l.cursor!=0):
            nodousuario.dato=extraerI(l)
            agregarDerecha(listaAux, nodousuario.dato)
        
        l=listaAux
        return listaAux

def agregarN(l, datoIngreso, n):
    listaAux = crearLista()
    
    nodousuario=Nodo()
    nodoAux=Nodo()
    if(estaVacia(l)):
        agregarDerecha(l, datoIngreso)
        return l
    else:
        i=0
        for i in range(n):
            nodoAux.dato= extraerI(l)
            agregarDerecha(listaAux, nodoAux.dato)
            print("se hace "+str(i)+"veces")
        
        nodousuario.dato=datoIngreso
        agregarDerecha(listaAux, datoIngreso)

        print("Fin del 1er while: ")
        l=recorrerLista(l)
        print("Fin lista original")
        listaAux= recorrerLista(listaAux)
        print("Fin lista nueva")
        while(l.cursor!=0):
            nodoAux.dato= extraerI(l)
            agregarDerecha(listaAux, nodoAux.dato)

    return listaAux


def extraerI(l):
    nodoAuxiliar = Nodo()
    if(estaVacia(l)):
        print("la lista está vacía")
        return None
    elif(l.cursor>1):
        nodoAuxiliar=l.cabecera
        l.cabecera=l.cabecera.siguiente
        l.cabecera.anterior=None
    elif(l.cursor==1):
        nodoAuxiliar=l.cabecera
        l.cabecera=None
        l.anterior=None
    
    l.cursor=l.cursor-1
    datoExtraido=nodoAuxiliar.dato
    del nodoAuxiliar
    return datoExtraido

def extraerD(l):
    listaAux=crearLista()
    
    
    if(estaVacia(l)):
        print("la lista está vacía")
        return None
    else:
        nodoAux=Nodo()
        i=0
        n=l.cursor
        for i in range(n):
            
            print("Veces: "+str(i))
            if(n-1!=i):
                nodoAux.dato=extraerI(l)
                agregarDerecha(listaAux, nodoAux.dato)
            else:
                nodoAux.dato=extraerI(l)
        datoExtraido=nodoAux.dato
        recorrerLista(listaAux)
        while(listaAux.cursor!=0):
            nodoAux.dato=extraerI(listaAux)
            agregarDerecha(l, nodoAux.dato)
            
    del nodoAux
    return datoExtraido



def extraerN(l, n):
    listaAux = crearLista()
    
    nodousuario=Nodo()
    nodoAux=Nodo()
    if(estaVacia(l)):
        print("la lista está vacía")
        return None
    else:
        i=0
        for i in range(n):
            nodoAux.dato= extraerI(l)
            agregarDerecha(listaAux, nodoAux.dato)
            print("se hace "+str(i)+"veces")
        
        nodoAux.dato= extraerI(l)
        datoExtraido=nodoAux.dato


        
        while(l.cursor!=0):
            nodoAux.dato= extraerI(l)
            agregarDerecha(listaAux, nodoAux.dato)

        while(listaAux.cursor!=0):
            nodoAux.dato=extraerI(listaAux)
            agregarDerecha(l, nodoAux.dato)

    del nodoAux
    return datoExtraido

def recorrerLista(l):
    if(estaVacia(l)):
        print("Está vacía")
        return l
    listaAux=crearLista()
    nodoAux = Nodo()
    nodoAux=l.cabecera
    while(nodoAux!=None):
        print(nodoAux.dato)
        agregarDerecha(listaAux, nodoAux.dato)
        nodoAux=nodoAux.siguiente
    return listaAux

def estaVacia(l):
    if(l.cabecera==None and l.cursor==0):
        return True
    else:
        return False

def contarNodos(l):
    return l.cursor

def borrarLista(l):
    if(estaVacia(l)==False):
        nodoAuxiliar = Nodo()
        nodoAuxiliarRespaldo = Nodo()
        nodoAuxiliar=l.cabecera
        while(nodoAuxiliar!=None):
            nodoAuxiliarRespaldo=nodoAuxiliar.siguiente
            del nodoAuxiliar
            nodoAuxiliar=nodoAuxiliarRespaldo
        l.cabecera=None
        l.cursor=None
        del l