"""
Palacios Elizondo Kevin Antonio
2BM1
Inteligencia Artificial
23/04/2022 
q:)->-</: 
"""
class Dato:
    def __init__(self):
        self.valor = None

class Nodo:
    def __init__(self):
        self.dato = Dato()
        self.pos = None
        self.siguiente = None
        self.anterior = None

class lista:
    def __init__(self, cursor):
        self.cursor = cursor
        self.cabecera = Nodo()