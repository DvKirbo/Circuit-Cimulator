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

class SimuladorCircuitos:
    def __init__(self):
        self.nodos = {}

    def crear_nodo(self, nombre, resistencia=None):
        if nombre not in self.nodos:
            if resistencia is None:
                nodo = Nodo(nombre)
            else:
                nodo = Resistencia(nombre, resistencia)
            self.nodos[nombre] = nodo
            return nodo
        else:
            print("El nombre del nodo ya existe. Por favor, elige otro nombre.")

    # Resto del código igual que antes...



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


# Ejemplo de uso
simulador = SimuladorCircuitos()
simulador.crear_nodo("A")
simulador.crear_nodo("B")
simulador.crear_nodo("C")
simulador.crear_nodo("R1", resistencia=100)
simulador.conectar_nodos("A", "B")
simulador.conectar_nodos("B", "C")
simulador.conectar_nodos("C", "R1")
simulador.imprimir_conexiones()
