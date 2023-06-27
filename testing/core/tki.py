import pygame



class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []

    def conectar(self, nodo):
        self.conexiones.append(nodo)
        nodo.conexiones.append(self)

    def desconectar(self, nodo):
        if nodo in self.conexiones:
            self.conexiones.remove(nodo)
            nodo.conexiones.remove(self)

    def __str__(self):
        return self.nombre
    

class Resistencia(Nodo):
    def __init__(self, nombre, resistencia):
        super().__init__(nombre)
        self.resistencia = resistencia

    def __str__(self):
        return f"{self.nombre} ({self.resistencia} ohm)"

class FuenteVoltaje(Nodo):
    def __init__(self, nombre, voltaje):
        super().__init__(nombre)
        self.voltaje = voltaje

    def __str__(self):
        return f"{self.nombre} ({self.voltaje} V)"
    
class Capacitor(Nodo):
    def __init__(self, nombre, capacitancia):
        super().__init__(nombre)
        self.capacitancia = capacitancia

    def __str__(self):
        return f"{self.nombre} ({self.capacitancia} F)"


class SimuladorCircuitos:
    def __init__(self):
        self.nodos = {}


    def crear_nodo(self, nombre, resistencia=None, voltaje=None, capacitancia=None):
        if nombre not in self.nodos:
            if resistencia is not None:
                nodo = Resistencia(nombre, resistencia)
            elif voltaje is not None:
                nodo = FuenteVoltaje(nombre, voltaje)
            elif capacitancia is not None:
                nodo = Capacitor(nombre, capacitancia)
            else:
                nodo = Nodo(nombre)
            self.nodos[nombre] = nodo
            return nodo
        else:
            print("El nombre del nodo ya existe. Por favor, elige otro nombre.")

    # Resto del código...

    def conectar_nodos(self, nombre1, nombre2):
        if nombre1 in self.nodos and nombre2 in self.nodos:
            nodo1 = self.nodos[nombre1]
            nodo2 = self.nodos[nombre2]
            nodo1.conectar(nodo2)
            print("Nodos conectados correctamente.")
        else:
            print("Uno o ambos nodos no existen. Por favor, crea los nodos primero.")

    def desconectar_nodos(self, nombre1, nombre2):
        if nombre1 in self.nodos and nombre2 in self.nodos:
            nodo1 = self.nodos[nombre1]
            nodo2 = self.nodos[nombre2]
            nodo1.desconectar(nodo2)
            print("Nodos desconectados correctamente.")
        else:
            print("Uno o ambos nodos no existen. Por favor, crea los nodos primero.")

    def imprimir_conexiones(self):
        for nombre, nodo in self.nodos.items():
            conexiones = ", ".join(str(n) for n in nodo.conexiones)
            print(f"{nombre}: {conexiones}")



    def verificar_serie(self, nodo1, nodo2):
        if isinstance(nodo1, Resistencia) and isinstance(nodo2, Resistencia):
            return True
        elif isinstance(nodo1, Capacitor) and isinstance(nodo2, Capacitor):
            return True
        else:
            return False




    def verificar_paralelo(self, nodo1, nodo2):
        for nodo in nodo1.conexiones:
            if isinstance(nodo, Resistencia) and isinstance(nodo2, Resistencia):
                return True
            elif isinstance(nodo, Capacitor) and isinstance(nodo2, Capacitor):
                return True
        return False




    def calcular_resistencia_total(self, nodo):
        resistencia_total = 0
        for conexion in nodo.conexiones:
            if isinstance(conexion, Resistencia):
                resistencia_total += 1 / conexion.resistencia

        if resistencia_total != 0:
            resistencia_total = 1 / resistencia_total

        return resistencia_total
    



    def calcular_capacitancia_total(self, nodo):
        capacitancia_total = 0
        for conexion in nodo.conexiones:
            if isinstance(conexion, Capacitor):
                capacitancia_total += conexion.capacitancia

        return capacitancia_total



    def calcular_voltaje(self, nodo):
        voltaje_total = 0
        for conexion in nodo.conexiones:
            if isinstance(conexion, FuenteVoltaje):
                voltaje_total += conexion.voltaje

        return voltaje_total
    


