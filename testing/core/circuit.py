import numpy as np

class CircuitSimulator:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_matrix = np.zeros((num_nodes, num_nodes))
        self.currents = np.zeros(num_nodes)
        self.voltages = np.zeros(num_nodes)

    def add_resistor(self, node1, node2, resistance):
        self.adj_matrix[node1, node1] += 1 / resistance
        self.adj_matrix[node2, node2] += 1 / resistance
        self.adj_matrix[node1, node2] -= 1 / resistance
        self.adj_matrix[node2, node1] -= 1 / resistance

    def add_current_source(self, node1, node2, current):
        self.currents[node1] -= current
        self.currents[node2] += current

    def solve(self):
        self.voltages = np.linalg.solve(self.adj_matrix, self.currents)
        return self.voltages

# Ejemplo de uso:
simulator = CircuitSimulator(3)
simulator.add_resistor(0, 1, 100)  # Resistencia de 100 Ohms entre nodo 0 y nodo 1
simulator.add_current_source(1, 2, 0.1)  # Fuente de corriente de 0.1 Amperios de nodo 1 a nodo 2
voltages = simulator.solve()
print("Voltajes en los nodos:", voltages)
