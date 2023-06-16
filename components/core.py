import pygame
import time 
import pymunk

nxC,nX2=0
def get_columns_rows(x,y):
    nxC=x
    nxC=y

class dot :
    def __init__(self, x , y) -> None:
        self.x = x
        self.y =y
        
    def get_x(self, x):
        pass
    def get_y (self, y):
        pass

class item:
    def __init__(self) -> None:
        pass


class circuitGUI:
    def __init__(self) -> None:
        pass

class description:
    def __init__(self) -> str:
        pass


class Errors:
    def __init__(self) -> None:
        ERROR_DISCONNECTED = "El circuito esta desonectado"
        ERROR_RESISTENCIA = "No hay voltaje en la resistencia"
        ERROR_VOLTAJE = "demasiado voltaje"
    
